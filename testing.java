import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class SchoolCertificateAutomation {

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "/Users/amritanandsingh/chromedriver");
        WebDriver driver = new ChromeDriver();

        try {
            login(driver);
            navigateToCertificates(driver);
            selectCertificateType(driver);
            selectStudent(driver);
            clickGenerate(driver);
            updateRemarks(driver);
            generateAndDownload(driver);
            validateCertificateHistory(driver);

        } finally {
            driver.quit();
        }
    }

    private static void login(WebDriver driver) {
        driver.get("https://accounts.teachmint.com/");
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement phoneNumberInput = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@type='text']")));
        phoneNumberInput.sendKeys("your_phone_number");
        WebElement sendOTPButton = driver.findElement(By.id("send-otp-btn-id"));
        sendOTPButton.click();
        WebElement otpInput = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//input[@data-group-idx='0']")));
        otpInput.sendKeys("your_otp");
        WebElement submitOTPButton = driver.findElement(By.id("submit-otp-btn-id"));
        submitOTPButton.click();
    }

    private static void navigateToCertificates(WebDriver driver) {
        WebElement certificatesTab = driver.findElement(By.xpath("//a[contains(text(),'Certificates')]"));
        certificatesTab.click();
    }

    private static void selectCertificateType(WebDriver driver) {
        WebElement certificateDropdown = driver.findElement(By.id("certificate-type-dropdown"));
        certificateDropdown.click();
        WebElement firstOption = driver.findElement(By.xpath("//div[@role='option'][1]"));
        firstOption.click();
    }

    private static void selectStudent(WebDriver driver) {
        WebElement searchField = driver.findElement(By.id("student-search"));
        searchField.sendKeys("Sam");
        WebElement samOption = driver.findElement(By.xpath("//div[contains(text(),'Sam')]"));
        samOption.click();
    }

    private static void clickGenerate(WebDriver driver) {
        WebElement generateButton = driver.findElement(By.xpath("//button[contains(text(),'Generate')]"));
        generateButton.click();
    }

    private static void updateRemarks(WebDriver driver) {
         WebElement remarksTextarea = driver.findElement(By.id("remarks-textarea"));
        remarksTextarea.sendKeys("This is a test remark.");
    }

    private static void generateAndDownload(WebDriver driver) {
        WebElement downloadButton = driver.findElement(By.xpath("//button[contains(text(),'Download')]"));
        downloadButton.click();
    }

    private static void validateCertificateHistory(WebDriver driver) {
        WebElement historyLink = driver.findElement(By.xpath("//a[contains(text(),'View History')]"));
        historyLink.click();
    }
}
