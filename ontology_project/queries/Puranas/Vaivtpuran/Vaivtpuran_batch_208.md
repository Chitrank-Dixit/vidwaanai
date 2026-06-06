# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 13.10302)
- **Original**: मालाओंसे संयुक्त मोरपंखका मुकुट उनके मस्तकको उस मण्डपकी श्रीवृद्धि कर रहे थे। उसके भीतर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10303)
- **Original**: सुशोभित कर रहा था। त्रिभज्ञ चूड़ा (चोटी) चन्दन, अगुरु, कस्तूरी और केसरके द्रवसे युक्त
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10304)
- **Original**: धारण किये वे उस रत्लमण्डपकों निहार रहे थे। मालती-मालाओंके समूहसे पुष्पशय्या तैयार की
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10305)
- **Original**: राधाने देखा मेरी गोदमें बालक नहीं है और उधर गयी थी। वहाँ नाना प्रकारकी भोगसामग्री संचित
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10306)
- **Original**: वे नूतन यौवनशाली पुरुष दृष्टिगोचर हो रहे हैं। थी। दीवारोंमें दिव्य दर्पण लगे हुए थे। श्रेष्ठ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10307)
- **Original**: यह देखकर सर्वस्मृतिस्वरूपा होनेपर भी राधाको मणियों, मुक्ताओं और माणिक्योंकी मालाओंके बड़ा विस्मय हुआ। रासेश्वरी उस परम मनोहर जालसे उस मण्डपको सजाया गया था। उसमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10308)
- **Original**: रूपको देखकर मोहित हो गयीं। वे प्रेम और मणीन्द्रसारचित किवाड़ लगे हुए थे। वह भवन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10309)
- **Original**: प्रसन्षताके साथ अपने लोचन-चकोरोंके द्वारा बेल-बूटोंसे विभूषित वस्त्रों और श्रेष्ठ पताका-
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10310)
- **Original**: उनके मुखचन्द्रकी सुधाका पान करने लगीं। समूहोंसे सुसज्जित था। कुंकुमके समान रंगवाली
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10311)
- **Original**: उनकी पलकें नहीं गिरती थीं। मनमें प्रेमविहारकी मणियोंद्वारा उसमें सात सीढ़ियाँ बनायी गयी थीं।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10312)
- **Original**: लालसा जाग उठी। उस समय राधाका सर्वाब्न उस भवनके सामने एक पुष्पोद्यान था, जो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10313)
- **Original**: पुलकित हो उठा। वे मन्द-मन्द मुस्कराती हुई भ्रमरोंके गुझारवसे युक्त पुष्पसमूहोंद्वारा शोभा पा
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10314)
- **Original**: प्रेम-बेदनासे व्यधित हो उठीं। तब तिरछी चितवनसे रहा था। देवी राधा उस मण्डपको देखकर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10315)
- **Original**: अपनी ओर देखती हुई, मुस्कराते मुखारविन्दवाली प्रसन्नतापूर्वक्क उसके भीतर चली गयों। वहाँ श्रीराधासे वहाँ श्रीहरिने इस प्रकार कहा। उन्होंने कर्पूर आदिसे युक्त ताम्बूल तथा रलमय
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10316)
- **Original**: श्रीकृष्ण बोले--राधे ! गोलोकमें देवमण्डलीके कलशमें रखा हुआ स्वच्छ, शीतल एबं मनोहर भीतर जो बृत्तान्त घटित हुआ था, उसका तुम्हें जल देखा। नारद! यहाँ सुधा और मधुसे भरे हुए
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10317)
- **Original**: स्मरण तो है न? प्रिये! पूर्वकालमें मैंने जो कुछ अनेक रत्ममय कलश शोभा पा रहे थे। उस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10318)
- **Original**: स्वीकार किया है, उसे आज पूर्ण करूँगा। सुमुखि भवनके भीतर पुष्पमयी शय्यापर एक किशोर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10319)
- **Original**: राधे! तुम मेरे लिये प्राणोंसे भी बढ़कर प्रियतमा अबस्थावाले श्यामसुन्दर कमनीय पुरुष सो रहे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10320)
- **Original**: हो। जैसी तुम हो, वैसा मैं हूँ; निश्चय ही हम थे, जो अत्यन्त मनोहर थे। उनके मुखपर मन्द
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10321)
- **Original**: दोनोंमें भेद नहीं है। जैसे दूधमें धवलता, अग्निमें मुस्कानकी छटा छा रही थी। वे चन्दनसे चर्चित
- **Translation**: 

---

