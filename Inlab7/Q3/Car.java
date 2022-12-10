package Q3 ;
/* 
 * AUTHOR: ASHWIN ABRAHAM
*/

/*
 * TODO: Create class Car along with proper methods and inheritance as required
 */

public class Car extends Vehicle
{
    Car(String rn, String man, String own)
    {
        super(rn, man, own);
    }

    public void checkPollutionStatus()
    {
        if(CO2 <= 15 && CO <= 0.5 && HC <= 750)
        {
            pollutionStatus = "PASS";
        }
        else
        {
            pollutionStatus = "FAIL";
        }
    }
}