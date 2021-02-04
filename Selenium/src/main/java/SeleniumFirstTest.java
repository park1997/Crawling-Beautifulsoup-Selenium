import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;


public class SeleniumFirstTest {
    WebDriver driver;

    public void launchBrowser(){
        System.setProperty("webdriver.gecko.driver","/usr/local/bin/geckodriver");
        driver = new FirefoxDriver();
        String url = "https://new.land.naver.com/complexes/1525";
        driver.get("https://new.land.naver.com/complexes/13261");
    }


    public static void main(String[] args) {
        SeleniumFirstTest obj = new SeleniumFirstTest();

        obj.launchBrowser();



    }
}
