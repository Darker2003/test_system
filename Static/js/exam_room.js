let currentQuestion = 1;
const totalQuestions = parseInt(document.getElementById('totalQuestions').innerHTML);
let answeredQuestions = [];

function answerQuestion(questionNumber) {
    const selectedAnswer = document.querySelector('input[name="q' + questionNumber + '"]:checked').value;

    // Check if the user has already answered the current question
    const existingAnswerIndex = answeredQuestions.findIndex(answer => answer.question === questionNumber);

    if (existingAnswerIndex !== -1) {
        // Update the existing answer
        answeredQuestions[existingAnswerIndex].answer = selectedAnswer;
    } else {
        // Add the new answer
        answeredQuestions.push({ question: questionNumber, answer: selectedAnswer });

        // Update progress
        document.getElementById('progress').innerText = answeredQuestions.length;
    }

    // Show next question or finish if all questions are completed
    const nextQuestionBox = document.getElementById('questionBox' + (questionNumber + 1));
    if (answeredQuestions.length < totalQuestions) {
        nextQuestionBox.scrollIntoView({ behavior: 'smooth' });
    } else {
        document.getElementById('submitButton').style.display = 'block';
    }
}

function submitQuiz() {
    // Disable radio buttons to lock the answers
    document.querySelectorAll('input[type="radio"]').forEach(function (element) {
        element.disabled = true;
    });

    // Hide progress box
    document.getElementById('progressBox').style.display = 'none';

    // Show completion message
    document.getElementById('completionMessage').style.display = 'block';

    // Hide submit button
    document.getElementById('submitButton').style.display = 'none';

    console.log(answeredQuestions); // Display the answered questions with their selected answers
    Save_Quiz(answeredQuestions)
}

function Save_Quiz(answeredQuestions) {
    // Get exam ID and course ID from the HTML elements
    let examId = document.getElementById('exam_id').innerText;
    console.log(examId);
    // Get CSRF token
    let csrfToken = document.getElementById('csrf_token').value;
    
    // Send JSON data to backend endpoint using AJAX
    fetch('/save_quiz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            exam_id: examId,
            json_data: answeredQuestions,
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to save JSON data');
        }
        return response.json();
    })
    .then(result => {
        // Handle success
        console.log('JSON data saved successfully:', result);
    })
    .catch(error => {
        // Handle error
        console.error('Error saving JSON data:', error);
    });
}
