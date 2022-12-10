package Q3 ;

/*
 * AUTHOR: ASHWIN ABRAHAM
*/

/*
 * TODO: Create class Truck along with proper methods and inheritance as required
 */

public class Truck extends Vehicle
{
    Truck(String rn, String man, String own)
    {
        super(rn, man, own);
    }

    public void checkPollutionStatus()
    {
        if(CO2 <= 25 && CO <= 0.8 && HC <= 1000)
        {
            pollutionStatus = "PASS";
        }
        else
        {
            pollutionStatus = "FAIL";
        }
    }
}