import { API_BASE_URL } from './config.js';

// Function to fetch and display company reviews
async function getCompanyReviews(companyName) {
  if (!companyName.trim()) {
    alert("Please enter a company name for reviews.");
    return;
  }

  // Open a new tab to display company reviews.
  const reviewTab = window.open("", "ReviewTab");
  reviewTab.document.write("<p>Loading reviews...</p>");

  try {
    // Call your Flask API for reviews
    const response = await fetch(`${API_BASE_URL}:5002/get_reviews`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ company_name: companyName })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    const data = await response.json();
    
    if (!data.review) {
      reviewTab.document.write("<h2>Error: No review data found.</h2>");
      return;
    }
    
    const reviews = data.review.reviews || {};
    const links = data.review.links || {};
    
    let htmlContent = `<h2>Reviews for ${companyName}</h2>`;
    for (const platform in reviews) {
      htmlContent += `<h3>${platform}</h3>`;
      htmlContent += `<p>${reviews[platform]}</p>`;
      htmlContent += `<a href="${links[platform]}" target="_blank">Read more on ${platform}</a><br><br>`;
    }
    
    reviewTab.document.body.innerHTML = htmlContent;
  }
  catch (error) {
    reviewTab.document.write(`<h2>Error fetching reviews: ${error.message}</h2>`);
    console.error("Review fetch error:", error);
  }
}

export { getCompanyReviews };