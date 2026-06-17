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

### Verse 1 (Vaivtpuran 13.10982)
- **Original**: गये, जहाँ ब्राह्मणियाँ भोजन बना रही थीं। उन खेलते-खेलते वे थक गये और उन्हें भूख-प्यास
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10983)
- **Original**: बालकोंने ब्राह्मणपत्नियोंको सिर झुकाकर प्रणाम सताने लगी। तब सब गोपशिशु बड़ी प्रसन्नताके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10984)
- **Original**: किया। प्रणाम करके वे सब बालक उन पतित्रता साथ श्रीकृष्णके पास आये और बोले--' कन्हैया !
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10985)
- **Original**: ब्राह्मणियोंसे बोले--'माताओ ! हम सब बालक हमें बड़ी भूख लगी है। हम सेवकोंको आज्ञा
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10986)
- **Original**: भूखसे पीडित हैं। हमें भोजन दो।' दो, क्‍या करें?' ग्वालबालॉंकी बात सुनकर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10987)
- **Original**: उन बालकोंकी बात सुनकर और उनकी प्रसन्नमुख और नेत्रवाले दयानिधान श्रीहरिने उनसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10988)
- **Original**: मनोहर आकृति देखकर उन सती-साध्यी ब्राह्मणियोंने यह हितकर तथा सच्ची बात कहीं। मुस्कराते हुए मुखारविन्दसे आदरपूर्वक पूछा। श्रीकृष्ण बोले--बालको ! जहाँ ब्राह्मणॉंका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10989)
- **Original**: ._ ब्राह्मणपत्नियाँ बोलीं--समझदार बालको ! सुखदायक यज्ञस्थान है, वहाँ जाओ। जाकर उन
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10990)
- **Original**: तुम लोग कौन हो ? किसने तुम्हें भेजा है? और “यज्ञतत्पर ब्राह्मणोंसे शीघ्र ही भोजनके लिये अन्न
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10991)
- **Original**: तुम्हारे नाम क्‍या हैं ? हम तुम्हें व्यज्गसहित नाना माँगी। वे सभी आज्लिरस गोत्रवाले ब्राह्मण हैं
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10992)
- **Original**: प्रकारका श्रेष्ठ भोजन प्रदान करेंगी। और श्रीवनके निकट अपने आश्रममें यज्ञ करते ब्राह्मणियोंकी बात सुनकर वे सभी स्िग्ध हैं। उन्होंने श्रुतियों और स्मृतियोंका विशेष ज्ञान
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10993)
- **Original**: एवं हृष्ट-पुष्ट गोपबालक प्रसन्नतापूर्वक हँसते प्राप्त किया है। वे सब निःस्पृह्ठ वैष्णव हैं और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10994)
- **Original**: हुए बोले। मोक्षकी कामनासे मेरा ही यजन कर रहे हैं। . बालकोंने कहा--माताओ! हमें बलराम परंतु मायासे आच्छादित होनेके कारण उन्हें इस
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10995)
- **Original**: और श्रीकृष्णने भेजा है। हमलोग भूखसे बहुत बातका पता नहीं है कि योगमायासे मनुष्यरूप
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10996)
- **Original**: पीड़ित हैं। हमें भोजन दो। हम शीघ्र ही उनके धारण करके प्रकट हुआ मैं ही उनका आराध्य
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10997)
- **Original**: पास लौट जायँगे। यहाँसे थोड़ी दूरपर बनके देव हूँ। केवल यज्ञकी ओर ही उन्मुख रहनेवाले
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10998)
- **Original**: भीतर भाण्डोर-वटके निकट मधुवनमें बलराम वे ब्राह्मण यदि तुम्हें अन्न न दें तो शीघ्र ही [और केशव बैठे हैं। वे दोनों भाई भी थके- जाकर उनकी पत्नियोंसे माँगना; क्योंकि वे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10999)
- **Original**: माँदे और भूखे हैं तथा भोजन माँग रहे हैं।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11000)
- **Original**: 490 *» संक्षिप्त अह्मवैवर्तपुराण
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11001)
- **Original**: ###&##%ऋऋऋऋऋकऋऋ/#%4%#######&###%ऋकऋऋऋऋऋकऋऋकऋऋकऋकऋककऋकऋकऋ कक अ्क्क्क् कक कक कक ऋफ़ ऋकक कक क क माताओ! आपको अन्न देना है या नहीं देना है,
- **Translation**: 

---

