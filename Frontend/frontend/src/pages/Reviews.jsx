import { useEffect, useState } from "react";
import API from "../services/api";

function Reviews() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetchReviews();
  }, []);

  const fetchReviews = async () => {
    const response = await API.get("reviews/reviews/");
    setReviews(response.data);
  };

  return (
    <div>
      <h1>Record Reviews</h1>

      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Reviewer</th>
            <th>Status</th>
            <th>Comment</th>
            <th>Round</th>
          </tr>
        </thead>

        <tbody>
          {reviews.map((review) => (
            <tr key={review.id}>
              <td>{review.id}</td>
              <td>{review.reviewer_name}</td>
              <td>{review.status}</td>
              <td>{review.reviewer_comment}</td>
              <td>{review.review_round}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Reviews;