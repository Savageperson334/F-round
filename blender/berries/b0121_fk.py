# fk
#
# Copied verbatim from https://github.com/CassGut/Kinova-Gen-3-Robotic-Arm-Pick-and-Place-Controller-Tutorial
#   notebook Part 2/4_0_Numerical_Inverse_Kinematics.ipynb (its code cells joined in order; line 347 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def Rx(theta):
    Rx_matrix = np.array([
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

    return Rx_matrix


def Rz(theta):
    Rz_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    return Rz_matrix


def T(dx, dy, dz):
    T_matrix = np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])
    return T_matrix


def round_to(number, precision):
    return np.where(np.abs(number) < precision, 0, number)


def fk(q_values):
    q1 = q_values[0];
    q2 = q_values[1];
    q3 = q_values[2];
    q4 = q_values[3];
    q5 = q_values[4];
    q6 = q_values[5];
    q7 = q_values[6];

    E1 = T(0, 0, 0.15643)
    E2 = Rx(np.pi)
    E3 = Rz(q1)
    E4 = T(0, 0, -0.12838)
    E5 = T(0, 0.00538, 0)
    E6 = Rx(np.pi/2)
    E7 = Rz(q2)
    E8 = T(0, 0, -0.00638)
    E9 = T(0, -0.21038, 0)
    E10 = Rx(-np.pi/2)
    E11 = Rz(q3)
    E12 = T(0, 0, -0.21038)
    E13 = T(0, 0.00638, 0)
    E14 = Rx(np.pi/2)
    E15 = Rz(q4)
    E16 = T(0, 0, -0.00638)
    E17 = T(0, -0.20843, 0)
    E18 = Rx(-np.pi/2)
    E19 = Rz(q5)
    E20 = T(0, 0, -0.10593)
    E21 = Rx(np.pi/2)
    E22 = Rz(q6)
    E23 = T(0, -0.10593, 0)
    E24 = Rx(-np.pi/2)
    E25 = Rz(q7)
    E26 = T(0, 0, -0.06153)
    E27 = Rx(np.pi)
    E28 = T(0.0089253606274724, 0.004642492, 0.120162814)


       # Intermediate variables
    terms = [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10,
         E11, E12, E13, E14, E15, E16, E17, E18, E19,
         E20, E21, E22, E23, E24, E25, E26, E27, E28]

    HTM = np.linalg.multi_dot(terms)

    return round_to(HTM,1e-13)
