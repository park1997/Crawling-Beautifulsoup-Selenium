import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;



public class Steemit {

    public static void main(String[] args) throws InterruptedException {
        WebDriver driver = new ChromeDriver();
        driver.get("https://steemit.com");

        Wait<WebDriver> wait = new WebDriverWait(driver, 10);

        Thread.sleep(2000);
        JavascriptExecutor je = (JavascriptExecutor) driver;
        je.executeScript("window.scrollTo(0, document.body.scrollHeight)");

        Thread.sleep(2000);
        je.executeScript("window.scrollTo(0, window.scrollY + 700)");

        Thread.sleep(2000);
        je.executeScript("document.getElementById('content').scrollIntoView(true)");

        Thread.sleep(2000);
        je.executeScript("window.scrollBy(0, document.body.scrollHeight)");

        Thread.sleep(2000);
        WebElement html = driver.findElement(By.tagName("html"));
        html.sendKeys(Keys.HOME);

        Thread.sleep(2000);
        html.sendKeys(Keys.PAGE_DOWN);

        Thread.sleep(2000);
        WebElement ele = driver.findElements(By.id("posts_list")).get(0);
        je.executeScript("arguments[0].scrollIntoView()",ele );
        driver.quit();
    }
}