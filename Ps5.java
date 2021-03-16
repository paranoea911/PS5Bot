import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.By.ByClassName;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

//import com.sun.java.util.jar.pack.DriverResource;

public class Ps5 {

	private static final By ByClassName = null;

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.setProperty("webdriver.chrome.driver", "/Users/Hassan/Downloads/chromedriver 8");
		WebDriver driver = new ChromeDriver();
		/*var wmt = "https://www.walmart.com/ip/PlayStation-5-Console/363472942";
				driver.get(wmt);
				driver.navigate().refresh();
				
				System.out.print(driver.getTitle());
				//driver.navigate().wait();
		//driver.get("https://www.walmart.com/ip/PlayStation-5-Console/363472942");
		System.out.println(driver.getTitle());
		//System.out.println(driver.getPageSource());
		System.out.println(driver.getCurrentUrl());
		driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
		driver.get(wmt);
		driver.get(wmt);
		driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);
		driver.get(wmt);
		driver.get(wmt);
		driver.get(wmt);
		//WebElement addtocart = driver.findElement(By.className ("spin-button-children"));
		//WebElement add = driver.findElement(ByClassName);
		//addtocart.click();
		
		var tgt = "https://www.target.com/p/playstation-5-console/-/A-81114595";
		var tg2 = "https://www.target.com/p/fifa-21-playstation-4-5/-/A-80369290";
		driver.get(tg2);
		//driver.findElement(By.className("Button__ButtonWithStyles-y45r97-0 styles__StyledButton-sc-1f2lsll-0 dGuFoY iIyhFg")).click();
		//driver.findElement(By.className("shipItButton")); */
		var amz= "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG";
		driver.get(amz); 
		driver.findElement(By.id("buy-now-button")).click();
		//driver.get("");
		
		WebElement email= driver.findElement(By.id("ap_email"));
		email.sendKeys("ahm2@gmail.com");
		email.sendKeys(Keys.ENTER);
		//driver.navigate().wait();
		
		WebElement pwd= driver.findElement(By.name("password"));
		pwd.sendKeys("pass999");
		pwd.sendKeys(Keys.ENTER);
				
	
		
		
		
		//var amz2 = "https://www.amazon.com/Assassins-Creed-Valhalla-PlayStation-5-Standard/dp/B08FS5HKTR/";
	
//		driver.get(amz2);
		//driver.findElement(By.id("add-to-cart-button")).click();
		
		
		
		
		

		
		
		
	}

}
