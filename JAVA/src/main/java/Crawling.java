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
            Thread.sleep(1000);
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
        System.out.println(size_infos);
        // "단지 내 면적별 정보" String
        String width_info_name = size_infos.select("h5.heading_text").text();
        System.out.println(width_info_name);









        // 결과 출력
        System.out.println(info);

        // 1초 쉬었다가 종료
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        driver.quit();
    }
}
