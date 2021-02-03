import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.io.IOException;
import java.util.HashMap;

public class SeleniumCrawling {
    WebDriver driver = new ChromeDriver();
    HashMap<String, String> info = new HashMap<>();
    JavascriptExecutor js = (JavascriptExecutor) driver;
    public static String url = "https://new.land.naver.com/complexes/1525";
    public static Document doc;

    public void loadBrowser() {
        // 드라이버 경로 설정 및
        System.setProperty("webdriver.gecko.driver", "/usr/local/bin/geckodriver");

        ChromeOptions options = new ChromeOptions();
        options.addArguments("headless");
        // 주소 가져오기 + 화면 열기
        driver.get(this.url);

        // 화면 최대화
        driver.manage().window().maximize();
    }

    public void quitBrowser() {
        // 1초 쉬었다가 종료
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        driver.quit();

    }

    // doc 객체 생성
    public static Document createSoup(String url) throws IOException{
        Document doc = Jsoup.connect(url).header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36").get();
        return doc;
    }


    public static void main(String[] args) throws IOException {

        SeleniumCrawling ob = new SeleniumCrawling();
        // 브라우저 실행
        ob.loadBrowser();

        // soup 생성
        doc = ob.createSoup(url);

//        System.out.println(doc);
        // 단지명
        Elements complex_title = doc.getElementsByTag("h3");





        // 브라우저 종료
        ob.quitBrowser();


    }

}
