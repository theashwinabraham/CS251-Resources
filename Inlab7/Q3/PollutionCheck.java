package Q3;

/*
 * AUTHOR: ASHWIN ABRAHAM
*/

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;

import javax.lang.model.util.ElementScanner6;

public class PollutionCheck {
    public static void main(String [] args) throws Exception {
        /*
         * Implement this function to produce the desired outputs
         */
        BufferedReader vehicle_reader = new BufferedReader(new FileReader(new File(args[0])));
        HashMap<String, Vehicle> License_to_vehicle = new HashMap<String, Vehicle>();
        String v_line;
        while((v_line = vehicle_reader.readLine()) != null)
        {
            String[] arr = v_line.split(", ");
            if(arr[3].equals("Car"))
            {
                License_to_vehicle.put(arr[0], new Car(arr[0], arr[1], arr[2]));
            }
            else if(arr[3].equals("Truck"))
            {
                License_to_vehicle.put(arr[0], new Truck(arr[0], arr[1], arr[2]));
            }
        }
        BufferedReader pollution_reader = new BufferedReader(new FileReader(new File(args[1])));
        String p_line;
        while((p_line = pollution_reader.readLine()) != null)
        {
            String[] arr = p_line.split(", ");
            if(License_to_vehicle.containsKey(arr[0]))
            {
                License_to_vehicle.get(arr[0]).setPollution(Double.parseDouble(arr[1]), Double.parseDouble(arr[2]), Double.parseDouble(arr[3]));
            }
        }
        BufferedReader query_reader = new BufferedReader(new FileReader(new File(args[2])));
        String q_line;
        while((q_line = query_reader.readLine()) != null)
        {
            if(License_to_vehicle.containsKey(q_line))
            {
                System.out.println(License_to_vehicle.get(q_line).getPollutionStatus());
            }
            else
            {
                System.out.println("NOT REGISTERED");
            }
        }
    }
}