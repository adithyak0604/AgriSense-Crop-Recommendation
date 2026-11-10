const form = document.getElementById("cropForm");

const results = document.getElementById("results");
const loading = document.getElementById("loading");
const errorBox = document.getElementById("errorBox");

const topCrop = document.getElementById("topCrop");
const latinName = document.getElementById("latinName");
const confidence = document.getElementById("confidence");
const reasonText = document.getElementById("reasonText");

const tipsList = document.getElementById("tipsList");
const recommendationList =
    document.getElementById("recommendationList");


form.addEventListener("submit", async function (event) {

    event.preventDefault();


    // Hide previous results/errors

    results.classList.add("hidden");

    errorBox.classList.add("hidden");

    loading.classList.remove("hidden");


    // Collect form data

    const data = {

        n: document.getElementById("n").value,

        p: document.getElementById("p").value,

        k: document.getElementById("k").value,

        temperature:
            document.getElementById("temperature").value,

        humidity:
            document.getElementById("humidity").value,

        ph:
            document.getElementById("ph").value,

        rainfall:
            document.getElementById("rainfall").value,

        season:
            document.getElementById("season").value
    };


    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });


        const result = await response.json();


        loading.classList.add("hidden");


        if (!result.success) {

            throw new Error(result.error);

        }


        displayResults(result.data);


    } catch (error) {

        loading.classList.add("hidden");

        errorBox.textContent =
            "Error: " + error.message;

        errorBox.classList.remove("hidden");

    }

});


function displayResults(data) {


    const best = data.top_crop;


    // Best crop

    topCrop.textContent =
        "🌾 " + best.crop;

    latinName.textContent =
        best.latin;

    confidence.textContent =
        best.confidence + "%";

    reasonText.textContent =
        best.reason;


    // Growing tips

    tipsList.innerHTML = "";

    best.tips.forEach(function (tip) {

        const li =
            document.createElement("li");

        li.textContent = tip;

        tipsList.appendChild(li);

    });


    // Other recommendations

    recommendationList.innerHTML = "";


    data.recommendations
        .slice(1)
        .forEach(function (item) {

            const div =
                document.createElement("div");

            div.className =
                "recommendation-item";


            div.innerHTML = `

                <div>

                    <span class="rank">
                        #${item.rank}
                    </span>

                    <strong>
                        ${item.crop}
                    </strong>

                    <p>
                        ${item.latin}
                    </p>

                </div>


                <div class="crop-confidence">

                    ${item.confidence}%

                </div>

            `;


            recommendationList.appendChild(div);

        });


    results.classList.remove("hidden");


    // Scroll smoothly to results

    results.scrollIntoView({
        behavior: "smooth"
    });

}