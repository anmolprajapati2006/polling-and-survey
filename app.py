<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Activity Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
        p {
            font-size: 18px;
            margin-top: 20px;
            color: #555;
        }
    </style>//commit7
</head>
<body>
    <div class="container">
        <h1>Random Activity Generator</h1>
        <button onclick="generateActivity()">Generate Random Activity</button>
        <p id="activity"></p>
    </div>
//commit6
    <script>
        // List of random activities
        const activities = [
            "Go for a walk in the park",
            "Read a book for 30 minutes",
            "Cook a new recipe",
            "Learn a new language phrase",
            "Practice a musical instrument for 20 minutes",
            "Write a short story or poem",
            "Try a new workout routine",
            "Do a random act of kindness for someone",
            "Visit a local museum or art gallery",
            "Start a journal and write down your thoughts",
            "Take a yoga or meditation session",
            "Call or video chat with a friend or family member",
            "Go for a bike ride around your neighborhood",
            "Volunteer for a local charity or organization"
        ];
//commit2
        // Function to generate a random activity
        function generateActivity() {
            const randomIndex = Math.floor(Math.random() * activities.length);
            document.getElementById("activity").innerText = activities[randomIndex];
        }//commit9
    </script>
    //commit
</body>
</html>
