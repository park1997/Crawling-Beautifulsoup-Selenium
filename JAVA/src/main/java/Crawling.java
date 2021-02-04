import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.ArrayList;
import java.util.HashMap;

public class Crawling {
    public static void main(String[] args) {
        ChromeDriver driver = new ChromeDriver();
        HashMap<String,String> info = new HashMap<>();
        JavascriptExecutor js = (JavascriptExecutor) driver;
        String url = "https://new.land.naver.com/complexes/1525";
//        Document doc = Jsoup.connect(url).userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36").get();
//        Document doc = Jsoup.connect(url).get();
        driver.get(url);
//        창 최대화
        driver.manage().window().maximize();

        /*
        스크롤 해야하는 영역
         */

        // 현재 페이지의 소스코드 가져오기
        Document doc = Jsoup.parse(driver.getPageSource());

        Elements complex_titles = doc.select("div.complex_title h3.title");
        System.out.println(complex_titles.size());

        // 단지명 : 해당 아파트
        info.put("단지명",complex_titles.get(0).text());

        // 단지 종류 : 아파트 , 오피스텔 ..
        Elements complex_type = doc.select("span.label--category");
        info.put("단지종류", complex_type.get(0).text());

        // 혹시나 발생할 버튼클릭에 있어서의 예외처리
        try{
            // "단지 정보" 라는 글자 저장
            String complex_info = driver.findElementByClassName("complex_link").getText();
            // 단지 정보 클릭!
            driver.findElementByClassName("complex_link").click();
        }catch(Exception e){
            e.printStackTrace();
        }

        // 현재 페이지의 소스코드 가져오기(페이지 소스 업데이트)
        doc = Jsoup.parse(driver.getPageSource());

        // Json 구조로 만들기위해 여러 인자들을 받을 리스트를 생성
        ArrayList<String> detail_infos_key = new ArrayList<>();
        ArrayList<String> detail_infos_value = new ArrayList<>();

        // 단지 정보 테이블 소스코드
        

        // for loop 을 이용하여 단지 정보 추출








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
