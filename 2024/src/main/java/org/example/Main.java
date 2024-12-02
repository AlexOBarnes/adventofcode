package org.example;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Collections;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        BufferedReader reader;
        String filepath = "src/data/day_1_input.txt";

        try {
            reader = new BufferedReader(new FileReader(filepath));
            String line;
            List<Integer> left = new ArrayList<>();
            List<Integer> right = new ArrayList<>();

            while ((line = reader.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                if (parts.length == 2) {
                    try {
                        // Parse the numbers and add them to their respective lists
                        int num1 = Integer.parseInt(parts[0]);
                        int num2 = Integer.parseInt(parts[1]);

                        left.add(num1);
                        right.add(num2);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid number format in line: " + line);
                    }
                } else {
                    System.out.println("Line does not have exactly two numbers: " + line);
                }
            }
            reader.close();
            Collections.sort(left);
            Collections.sort(right);
            int totalDifference = 0;
            for (int i = 0; i < left.size(); i++) {
                totalDifference += Math.abs(left.get(i) - right.get(i));}
            System.out.println(totalDifference);
            Map<Integer, Integer> counter = new HashMap<>();
            for (int num : right) {
                counter.put(num, counter.getOrDefault(num, 0) + 1);
            }
            int total = 0;
            for (int num : left) {
                // Check if the current number exists in the counter
                if (counter.containsKey(num)) {
                    // Multiply the value in the counter by the current number from the left list
                    total += num * counter.get(num);
                }}
            System.out.println(total);
        } catch (IOException e) {
            System.out.println("IO Error!" + e.getMessage());
        }
        }
    }
