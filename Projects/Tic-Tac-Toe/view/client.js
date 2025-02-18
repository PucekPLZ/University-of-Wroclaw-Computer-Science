$(document).ready(function () {
    var game = {};
    var nickname;

    $("#board").hide();
    $("#remake").hide();

    var socket = io();

    const gameId = getGameId();
    if (gameId) {
        $("#status").html("Enter your nickname to join the game.");
        $("#nickname").show();
        $("#submitNickname").show();
        $("#howToPlay").hide();
    }

    var storedNickname = sessionStorage.getItem("nickname");
    if (storedNickname) {
        nickname = storedNickname;
        
        $("#nickname").hide();
        $("#submitNickname").hide();
        $("#status").html("Welcome, " + nickname);

        const gameId = getGameId();
        if (gameId) {
            socket.emit("join", { gameID: gameId, nickname: nickname });
        } else {
            $("#create").show();
            $("#findGames").show()
        }
    } else {
        $("#nickname").show();
        $("#submitNickname").show();
    }

    $("#submitNickname").on("click", function () {
        var enteredNickname = $("#nickname").val().trim();

        if (enteredNickname) {
            nickname = enteredNickname;
            
            sessionStorage.setItem("nickname", nickname);
            $("#status").html("Nickname set to: " + nickname);
            $("#nickname").hide();
            $("#submitNickname").hide();
    
            const gameId = getGameId();
            if (gameId) {
                socket.emit("join", { gameID: gameId, nickname: nickname });
            } else {
                $("#create").show();
                $("#findGames").show(); 
            }
        } else {
            $("#status").html("Enter a nickname.");
        }
    });  

    $("#create").on("click", function () {
        socket.emit("create", { nickname: nickname });
        $(".item").hide();
    });

    $("#findGames").on("click", function() {
        $(".item").hide(); 
        $("#availableGames").show();
        socket.emit("requestAvailableGames");
    });
 
    $("#remake").on("click", function () {
        socket.emit("restart", { id: game.id });
    });
    
    socket.on("created", function (data) {
        const url = window.location.href + "?gameId=" + data.id;
        $("#status").html(`Send this link to other player:`);
        $("#link").text(url);
        $('#link').show();
    });

    socket.on("availableGames", function(games) {
        $("#availableGames").show();
        var gameList = $("#gameList");
        gameList.empty();

        games.forEach(function(game) {
            var joinButton = $("<button>").text(`Join Game ${game.id}`);
            joinButton.on("click", function() {
                joinGame(game.id);
            });
            gameList.append(joinButton); 
        });
    });
    
    socket.on("start", function (data) {
        $("#remake").hide();
        $(".item").hide();
        $("#link").hide();

        game.id = data.id;
        game.board = data.gameboard;
        game.player = data.player;

        game.player1Nickname = data.player1Nickname;
        game.player2Nickname = data.player2Nickname;

        $("#board").show();
        updateGameboard();
    });

    socket.on("failed", function () {
        $("#status").html("GameID not found. Try again");
        $(".title").hide();
        $("#create").hide();
    });

    socket.on("invalid", function () {
        $("#status").html("Not a valid move.");
    });

    $("table").on("click", function (e) {
        let cellClicked = e.target.id;

        if (game.player.turn === true) {
            if (game.board[cellClicked] === "") {
                let data = { id: game.id, cell: cellClicked, player: game.player };
                socket.emit("move", data);
            } else {
                $("#status").html("Click an empty cell.");
            }
        } else {
            $("#status").html("Wait for other player.");
        }
    });

    socket.on("updateGame", function (data) {
        game.player.turn = !game.player.turn;
        game.board = data.gameboard;

        updateGameboard();
    });

    socket.on("win", function (data) {
        game.board = data;
        updateGameboard();

        $("#status").html("YOU WON!!!!");
        $("#remake").show();
    });

    socket.on("loss", function (data) {
        game.board = data;
        updateGameboard();

        $("#status").html("YOU LOST. GG.");
        $("#remake").show();
    });
   
    socket.on("tie", function (data) {
        game.board = data.gameboard;
        updateGameboard();

        $("#status").html("Tie.");
        $("#remake").show();
    });

    socket.on("quit", function () {
        $("#status").html("Connection Lost.");
        $("#board").hide();
        $(".item").show();
        $(".title").hide();
        $("#remake").hide();
    });

    function updateGameboard() {
        $.each(game.board, function (key, value) {
            if (value == "X") {
                $("#" + key).removeClass("red").addClass("blue");
            } else {
                $("#" + key).removeClass("blue").addClass("red");
            }
            $("#" + key).html(value);
        });

        
        if (game.player.turn) {
            $("#status").html("Your turn.");
        } else {
            let otherPlayerNickname = game.player.type === 'X' ? game.player2Nickname : game.player1Nickname;
            $("#status").html(otherPlayerNickname + "'s turn.");
        }
    }
    
    function joinGame(gameID) {
        socket.emit("join", { gameID: gameID, nickname: nickname });
        $("#availableGames").hide();
    }
});