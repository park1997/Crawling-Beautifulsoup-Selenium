import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.ArrayList;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import org.openqa.selenium.support.ui.Select;

import static org.openqa.selenium.Keys.PAGE_DOWN;


public class ex01 {
    public static void main(String[] args) throws InterruptedException {
        ChromeDriver driver = new ChromeDriver();
        // 정체 정보가 들어갈 Json
        JSONObject info = new JSONObject();
        JavascriptExecutor js = (JavascriptExecutor) driver;
        String url = "https://new.land.naver.com/complexes/1525";
        // Chrome 열기
        driver.get(url);

        // Chrome 창 최대화
//        driver.manage().window().maximize();

//        현재 페이지의 소스코드 가져오기
        Document doc = Jsoup.parse(driver.getPageSource());

        // 잠깐 쉬는 초 2 초
        int interval = 2000;

        JavascriptExecutor jse = (JavascriptExecutor)driver;

        jse.executeScript("window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight));");

        Object scrollwrap = js.executeScript("document.querySelector('.item_list.item_list--article');");

        Thread.sleep(interval);



        driver.close();




    }
}
