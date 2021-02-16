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
import java.util.Arrays;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import org.openqa.selenium.support.ui.Select;

import static org.openqa.selenium.Keys.PAGE_DOWN;


public class ex01 {
    public static void main(String[] args) throws InterruptedException {

        String ex = "95/75, 1/22층, 남향";
        String[] split = ex.split(",");
        System.out.println(Arrays.toString(split));
        System.out.println(split[0]);


    }
}
