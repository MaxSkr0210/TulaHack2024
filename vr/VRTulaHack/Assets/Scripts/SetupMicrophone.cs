using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SetupMicrophone : MonoBehaviour
{
    public Dropdown micDropdown;
    void Start()
    {
        // Загружаем dropdown вариантами
        string[] mics = Microphone.devices;

        micDropdown.options.Clear();
        foreach (var mic in mics)
        {
            micDropdown.options.Add(new Dropdown.OptionData() { text = mic });
        }
        Debug.Log(mics);
        //MicSelected(micDropdown);
        //       micDropdown.onValueChanged.AddListener(delegate {

        //           MicSelected(micDropdown);
        //};)
        Debug.Log(mics);
    }

    void Update()
    {
        
    }

    public void MicChoice()
    {
        
    }
}
