
# #Day 18 Homework
# #Homework 2
# #Fast Fourier Transform (FFT)

import numpy as np
import pylab as py

N=100

ti=-4.0
tf=4.0
t=np.linspace(ti,tf,N)
dt=t[1]-t[0]

f0=3.0
f=np.fft.fftfreq(N, dt)

def Function(T):
    return np.cos(2*np.pi*f0*T)*np.exp(-T**2)
    
ak=Function(t)
A=np.fft.fft(ak,norm="ortho")

py.figure(1)
py.plot(f,np.real(A),"-")
py.title("Fourier Real Plot")
py.xlabel("f", fontsize=16)
py.ylabel("A(f)", fontsize=16)
py.show()

py.figure(2)
py.plot(f,np.imag(A),"-")
py.title("Fourier Imaginary Plot")
py.xlabel("f", fontsize=16)
py.ylabel("A(f)", fontsize=16)
py.show()

py.figure(3)
py.plot(f,np.real(A)**2,"-")
py.title("Periodogram")
py.xlabel("t", fontsize=16)
py.ylabel("P(t)", fontsize=16)
py.show()