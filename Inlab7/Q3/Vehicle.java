package Q3;

/*
 * AUTHOR: ASHWIN ABRAHAM
*/

/*
 * TODO: Create class Vehicle along with given attributes and methods 
 */

public abstract class Vehicle {
    private String regNo, manufacturer, owner;
    protected String pollutionStatus;
    protected double CO2, CO, HC;

    Vehicle(String rn, String man, String own)
    {
        regNo = rn;
        manufacturer = man;
        owner = own;
        pollutionStatus = "PENDING";
    }

    public void setPollution(double co2, double co, double hc)
    {
        CO2 = co2;
        CO = co;
        HC = hc;
        checkPollutionStatus();
    }

    public String getPollutionStatus()
    {
        return pollutionStatus;
    }

    public abstract void checkPollutionStatus();
    public String toString()
    {
        return String.format("Reg No: %s\nManufacturer: %s\nOwner: %s\nPollution Status: %s\n", regNo, manufacturer, owner, pollutionStatus);
    }
}