import React, { useState } from 'react';

const Cart = () => {
    const [cart, setCart] = useState([]);

    const removeItem = (productId) => {
        setCart(cart.filter(item => item.product_id !== productId));
    };

    return (
        <div>
            <h1>Cart</h1>
            {cart.map(item => (
                <div key={item.product_id}>
                    <p>Product ID: {item.product_id}</p>
                    <p>Quantity: {item.quantity}</p>
                    <button onClick={() => removeItem(item.product_id)}>Remove</button>
                </div>
            ))}
        </div>
    );
};

export default Cart;
