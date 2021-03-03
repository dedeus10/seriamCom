
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// LIBRARIES -----------------------------------------------------------------------------
#include <compat/deprecated.h> // This contains several items that used to be available in
                               //previous versions of this scketch, but have eventually
                               //been deprecated over time.
#include <FlexiTimer2.h> // This library enable Arduino to use timer 2 with configurable
                         //resolution. http://www.arduino.cc/playground/Main/FlexiTimer2

// CONSTANTS -----------------------------------------------------------------------------
#define SAMPFREQ 90              // ADC sampling rate. CHANGE SAMPLE FREQ HERE
#define TIMER2VAL (1024/SAMPFREQ) // Set ADC sample rate frequency
#define TXSPEED 57600             // Serial communication speed. USE 57600
// ---

// GLOBAL VARIABLES ----------------------------------------------------------------------
volatile unsigned int ADC_Value = 0;     // ADC current value

// FUNCTIONS -----------------------------------------------------------------------------

// This is used to read values and send data over serial communication
void timerTwoOverflowISR(){
    //Read data from the serial
    Serial.println(analogRead(A0));
}

// ARDUINO SETUP and LOOP ----------------------------------------------------------------
// In setup arduino will initializes all peripherals
void setup(){
  // Disable all interrupts before initialization
  noInterrupts();
  
  pinMode(9, INPUT); // Setup for leads off detection LO +
  pinMode(10, INPUT); // Setup for leads off detection LO -

  // Set Timer2, that is used to setup the analag channels sampling frequency
  //and packet update. Whenever interrupt occures, the current read packet is
  //sent over serial communication.
  FlexiTimer2::set(10, timerTwoOverflowISR);
  FlexiTimer2::start();

  // Starts the communication with the previously defined speed
  Serial.begin(TXSPEED);

  // Enable all interrupts after initialization has been completed
  interrupts();
}

// In principal loop MCU will be put into sleep mode
void loop() {
  __asm__ __volatile__ ("sleep");
}
