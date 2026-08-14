function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {
            cookie = cookie.trim();

            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }

    return cookieValue;
}


async function askGramaSetuAI() {

    const questionInput = document.getElementById("aiQuestion");
    const answerCard = document.getElementById("aiAnswerCard");
    const answerText = document.getElementById("aiAnswerText");
    const askButton = document.getElementById("askAIButton");

    const question = questionInput.value.trim();

    // Check empty question
    if (!question) {
        answerCard.style.display = "block";
        answerText.innerText = "Please enter your question.";
        return;
    }

    // Show card
    answerCard.style.display = "block";

    // Loading message
    answerText.innerText = "GramaSetu AI is thinking...";

    // Disable button
    askButton.disabled = true;
    askButton.innerText = "Thinking...";

    try {

        const response = await fetch("/ai/ask-ai/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },

            body: JSON.stringify({
                question: question
            })
        });


        const data = await response.json();

        console.log("AI Response:", data);


        if (response.ok && data.success) {

            answerText.innerText = data.answer;

        } else {

            answerText.innerText =
                data.error || "Unable to get an answer.";

        }

    } catch (error) {

        console.error("AI Error:", error);

        answerText.innerText =
            "Something went wrong. Please try again.";

    } finally {

        askButton.disabled = false;
        askButton.innerText = "Ask AI";

    }
}