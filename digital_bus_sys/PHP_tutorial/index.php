<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First PHP Page</title>
</head>
<body>
    <h1>My PHP Test Page</h1>
    <!-- opening PHP -->
    <?php
        // Write PHP code here. 

        /*
            This is a block comment in PHP
        */

        $var = "Hello World!";
        $mark = 75;

        echo "The value is: <b><i>" . $var . "</i></b>"; // plus sign == '.' & can add html code

        echo "<p>"; // echo command to print the code

        if ($mark > 50) {
            echo "Congrats, you passed!";
        } else {
            echo "Sorry, you <i>didn't</i> pass!";
        }

        echo "</p>":

        // Call the function
        echo "<span>Your grade is :" . determinGrade($mark) . "</span>";

        // How to write function in PHP
        function determinGrade($result){
            $grade = "";

            if ($result >= 50) {
                $grade = "PA";
            } else {
                $grade = "NN";
            }

            return $grade;
        }

    ?> 
    <!-- closing PHP -->
</body>
</html>