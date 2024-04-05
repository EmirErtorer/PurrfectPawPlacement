from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test1(request):
    return HttpResponse("""
    <head>
    <title> My first website </title>
    <meta name="description" content="Free HTML tutorial">
    <meta name="keywords" content="HTML,tutorial,beginners">
    <meta name="author" content="BroCode">
    <meta name="viewport" content="width=device-width, initialscale=1.0">
    <meta charset="UTF-8">
</head>

<body style="background-color: black;">
    <h1> UR MOM</h1>

    <hr>

    <p> <span style="color: red">Lorem ipsum</span> dolor sit amet consectetur adipisicing elit. Labore harum unde incidunt. Officia consectetur eius, magni amet perferendis delectus reiciendis molestiae ut consequuntur, repellat pariatur dolore, et praesentium itaque nobis? </p>

    <audio controls autoplay src = "jjba.mp3"></audio>

    <br>

    <video controls autoplay mute src="unknown_replay_2023.07.13-18.35.mp4" width="450"></video>

    <h3>Mother of all Lists</h3>
    <ol type="i">
        <li>Your mom</li>
            <ul>
                <li>Very nice to me</li>
                <li>Stuff here</li>
            </ul>
        <li>My mom</li>
            <ul>
                <li>Is a big meanie to me :(</li>
                <li>Loves yemek</li>
            </ul>
    </ol>

    <table bgcolor="black" width="280">
        <tr bgcolor="lightgray" align="center">
            <th width="90"> Game </th>
            <th width="40"> Me Like? </th>
        </tr>
        <tr bgcolor="grey" align="center">
            <td width="90">Dark Souls 1</td>
            <td width="45">Yesss</td>
        </tr>
        <tr bgcolor="grey" align="center">
            <td width="90">Dark Souls 2</td>
            <td width="45">HELL NO</td>
        </tr>
    </table>

    <iframe src="https://www.protondb.com/" width="750" height="550"> </iframe>

    <br>

    <a href="https://en.wikipedia.org/wiki/Thylacine">
        <img src="tasmanian_tiger.jpeg" width="480">
    </a>

</body>
    
    """)