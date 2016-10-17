/*
 
   Temperature Converter Application

*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
		
		
public class TemperatureConverter extends JApplet implements ActionListener
{
	
	/// Class Variables:
	JPanel mainPanel;
	JLabel lbl;
	JTextField tf;
	JButton bt;
	
	
	/// Class Methods:
	
	public TemperatureConverter()
	{
		// Constructor:
		
		
	}
	
	
	public void init()
	{
		// Post: 
		
		mainPanel = (JPanel) getContentPane();
		mainPanel.setLayout( new FlowLayout() );
		mainPanel.setBackground( Color.lightGray );
		
		lbl = new JLabel("Write text here:");
		tf  = new JTextField("Input text", 20);
		bt  = new JButton("Press Me");
		
		lbl.setBackground( Color.green );
		lbl.setOpaque(true);
		
		mainPanel.add(lbl);
		mainPanel.add(tf);
		mainPanel.add(bt);
		
		bt.addActionListener( this );
		tf.addActionListener( this );
		
		validate();
		tf.requestFocus();
		
	}
	
	
	public void actionPerformed( ActionEvent ev )
	{
		// Post:
		
		mainPanel.setBackground( Color.darkGray );
		lbl.setText( lbl.getText() );
	}
	
}