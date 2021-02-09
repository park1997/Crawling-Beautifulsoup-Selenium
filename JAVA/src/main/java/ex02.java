import com.sun.security.jgss.GSSUtil;
import org.json.simple.JSONObject;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.chrome.ChromeDriver;

import static java.lang.Thread.sleep;

public class ex02 {
    public static void main(String[] args) throws InterruptedException {
        ChromeDriver driver = new ChromeDriver();
        JavascriptExecutor js = (JavascriptExecutor) driver;
        String url = "https://new.land.naver.com/complexes/113853";
        // Chrome 열기
        driver.get(url);

        // Chrome 창 최대화
        driver.manage().window().maximize();










        Thread.sleep(1000);

        driver.quit();


    }
}
