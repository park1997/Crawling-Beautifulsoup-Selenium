import jdk.swing.interop.SwingInterOpUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.ArrayList;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
public class Crawling {
    public static void main(String[] args) {
        int interval =1000;


        ChromeDriver driver = new ChromeDriver();
        // 정체 정보가 들어갈 Json
        JSONObject info = new JSONObject();
        JavascriptExecutor js = (JavascriptExecutor) driver;
        String url = "https://new.land.naver.com/complexes/1525";
//        Document doc = Jsoup.connect(url).userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36").get();
//        Document doc = Jsoup.connect(url).get();

        // Chrome 열기
        driver.get(url);

        // Chrome 창 최대화
        driver.manage().window().maximize();

        /*
        스크롤 해야하는 영역

        코
        드
        짜
        자

         */


        // 현재 페이지의 소스코드 가져오기
        Document doc = Jsoup.parse(driver.getPageSource());

        // 단지명 : 해당 아파트
        Elements complex_titles = doc.select("div.complex_title h3.title");
        info.put("단지명",complex_titles.get(0).text());

        // 단지 종류 : 아파트 , 오피스텔 ..
        Elements complex_type = doc.select("span.label--category");
        info.put("단지종류", complex_type.get(0).text());


        String complex_info = "";
        // 혹시나 발생할 버튼클릭에 있어서의 예외처리
        try{
            // "단지 정보" 라는 글자 저장
            complex_info = driver.findElementByClassName("complex_link").getText();
            // 단지 정보 클릭!
            driver.findElementByClassName("complex_link").click();
            // 혹시 모를 로딩으로 인해 1초 쉬어줌
            Thread.sleep(interval);
        }catch(Exception e){
            e.printStackTrace();
        }

        // 현재 페이지의 소스코드 가져오기(페이지 소스 업데이트)
        doc = Jsoup.parse(driver.getPageSource());

        // Json 구조로 만들기위해 여러 인자들을 받을 리스트를 생성
        JSONObject detail_info = new JSONObject();

        // temp
        ArrayList<String> key_temp = new ArrayList<>();
        ArrayList<String> value_temp = new ArrayList<>();


        // 단지 정보 테이블 소스코드
        Elements complex_infos = doc.select("div.detail_box--complex table.info_table_wrap tr.info_table_item");
//        System.out.println(complex_infos.size());

        // for loop 을 이용하여 단지 정보 추출
        for(Element detail_complex_info : complex_infos){
            // 단지 정보 key(세대수, 저/최고층, 사용승인일, 총주차대수, 용적률, 건폐율, ...)
            for(Element detail : detail_complex_info.select("th.table_th")){
                key_temp.add(detail.text());
//                System.out.println(detail.text());
            }
            // 단지 정보 value
            for(Element detail : detail_complex_info.select("td.table_td")){
                value_temp.add(detail.text());
//                System.out.println(detail.text());
            }
        }

        for(int i =0; i<key_temp.size();i++){
            detail_info.put(key_temp.get(i), value_temp.get(i));
        }

        info.put(complex_info,detail_info);

        // 나중에 다시 쓰기위해 초기화 함(Json)
        detail_info=null;
        // 해당면적 매물 : [매매 1, 전세2 ..] 와 같이 표현하기 위한 ArrayList 공간
        ArrayList<String> item_detail_info = new ArrayList<>();


        // "단지 내 면적별 정보" 테이블
        Elements size_infos = doc.select("h5.heading_text");
        // 위 테이블에서 뽑아낸 "단지 내 면적별 정보" String
        String width_info_name = doc.select("div.detail_box--floor_plan div.heading h5.heading_text").text().strip();



        Elements width_info = doc.select("div.detail_box--floor_plan a.detail_sorting_tab");
        JSONObject small_info = new JSONObject();
        for (int num = 0; num < width_info.size(); num++) {
            JSONObject obj_temp = new JSONObject();
            // click 을 위한 xpath 설정
            String xpath = String.format("//*[@id=\"tab%d\"]", num);
            // tab을 클릭함
            driver.findElementByXPath(xpath).click();

            // 탭 클릭때마다 0.1초 쉼
            // 0.1초만 쉬어도 돌아가는것을 확인했음!
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            // 현재 페이지의 소스코드 가져오기(페이지 소스 업데이트)
            doc = Jsoup.parse(driver.getPageSource());


            // 공급/전용, 방수/욕실수, 해다연적 세대수.. 등 에 대한 정보 table
            Elements size_infos_table = doc.select("div.detail_box--floor_plan table.info_table_wrap tr.info_table_item");
            // rowspan = 2 인 경우를 구별하기위한 boolean
            boolean checking_boolean = true;

            String title_for_rowspan = null;

            // 단지내 면적별 정보를 담기 위한 JSOUP
            /*
            77m:{xx:xx,
                yy:yy,
                ...
                zz:zz}
             */
            JSONObject obj_detail = new JSONObject();

            // 단지정보 -> 단지 내 면적별 정보 전체 크롤링 하기위한 for loop
            for(Element details_table : size_infos_table){
                // 데이터가 잠깐 담길 지역변수
                String title = null;
                String detail = null;
                JSONArray temp_array = new JSONArray();
                // 여기서 오류가 발생할 확률이 있으므로 예외처리로 오류가 발생하면 정보 못가져오게 !
                // 매물마다 있는 정보가 있고 없는 정보가 있기때문에 오류가 발생 할 수도(?) 있음
                try{
                        // 공급/ 전용, 방수/욕실 수, 해당면적 세대수, 현관구조, 공시가격
                    if (details_table.select("th.table_th").size() != 0 && details_table.select("td.table_td").size() != 0 && (checking_boolean) && (details_table.select("th[rowspan=2]").size() == 0)) {
                        title = details_table.select("th.table_th").text();
                        if (details_table.select("strong").size() != 0) {
                            detail = details_table.select("strong").text();
                        }else{
                            detail = details_table.select("td.table_td").text();
                        }
                        obj_detail.put(title, detail);
                        // 해당면적 매물, 관리비, 보유세
                    }else if (details_table.select("th[rowspan=2]").size() != 0 && checking_boolean && details_table.select("a").size() != 0) {
                        // 소 분류 이름
                        title = details_table.select("th[rowspan=2]").text();
                        // rowspan으로 인해 다음 태그에서 title 값을 못가져오므로 다른 변수에 타이틀 값 저장
                        title_for_rowspan = title;
                        Elements detail_infos = details_table.select("a.data");
                        String detail_info_name = null;
                        String detail_info_num = null;
                        for(Element elem : detail_infos){
                            detail_info_name = elem.text();
                            detail_info_num = elem.text();
                            temp_array.add(detail_info_name+" : "+detail_info_num);
                        }
                        obj_detail.put(title, temp_array);
                        checking_boolean = false;
                        // rowspan = 2 다음태그, 해당면적 매물, 관리비, 보유세
                    }else if (!(checking_boolean) && (details_table.select("ul").size() != 0)){
                        Elements detail_infos = details_table.select("li.info_list_item");
                        for(Element elem : detail_infos){
                            detail = elem.text().strip();
                            temp_array.add(detail);
                        }
                        obj_detail.put(title_for_rowspan, temp_array);
                        checking_boolean = true;
                        title_for_rowspan = null;
                        // 보유세 지역 크롤링 ( a 태그가 없는 것이 특징 !)
                    } else if (checking_boolean && details_table.select("th.table_th").size() != 0 && details_table.select("th[rowspan=2]").size() != 0 && details_table.select("a").size() == 0) {
                        title = details_table.select("th.table_th").text();
                        title_for_rowspan = title;
                        detail = details_table.select("strong").text();
                        temp_array.add(detail);
                        checking_boolean = false;
                        obj_detail.put(title, temp_array);
                    }
                }catch (IllegalStateException e){
                    e.printStackTrace();
                }
            }
            // Jsoup 형태로 저장
            small_info.put(width_info.get(num).text(), obj_detail);
        }
        // Jsoup 형태로 저장
        info.put(width_info_name,small_info);








        // 결과 출력
        System.out.println(info);

        // 1초 쉬었다가 종료
        try {
            Thread.sleep(interval);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        driver.quit();
    }
}
