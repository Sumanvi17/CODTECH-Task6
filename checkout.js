import React, { useState } from 'react';
import { loadStripe } from '@stripe/stripe-js';
import { Elements, CardElement, useStripe, useElements } from '@stripe/react-stripe-js';
import api from '../api';

const stripePromise = loadStripe('your-stripe-publishable-key');

const CheckoutForm = () => {
    const stripe = useStripe();
    const elements = useElements();
    const [errorMessage, setErrorMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        const { error, paymentIntent } = await stripe.confirmCardPayment(
            "client-secret-from-backend", {
                payment_method: {
                    card: elements.getElement(CardElement),
                },
            }
        );

        if (error) {
            setErrorMessage(error.message);
        } else if (paymentIntent.status === 'succeeded') {
            alert('Payment Successful!');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <CardElement />
            <button type="submit" disabled={!stripe}>
                Pay
            </button>
            {errorMessage && <p>{errorMessage}</p>}
        </form>
    );
};

const Checkout = () => (
    <Elements stripe={stripePromise}>
        <CheckoutForm />
    </Elements>
);

export default Checkout;
