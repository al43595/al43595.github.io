// src/components/ActionButton.js
import React from 'react';
import Button from '@material-ui/core/Button';

const ActionButton = ({ label, onClick }) => (
    <Button variant="contained" color="primary" onClick={onClick}>
        {label}
    </Button>
);

export default ActionButton;
