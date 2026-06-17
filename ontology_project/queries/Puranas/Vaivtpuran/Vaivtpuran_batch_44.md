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

### Verse 1 (Vaivtpuran 4.8927)
- **Original**: होते हैं। उनके शिखर बहुमूल्य रत्रमय कलश- थे, जो भाँति-भाँतिके नृत्यके प्रदर्शका मनोरथ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 4.8928)
- **Original**: समूहोंसे जाज्वल्यमान हैं। उत्तम रब्रोंद्वारां उनकी लिये खड़ी थीं। नारद! कुछ दूर और आगे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 4.8929)
- **Original**: रचना हुई है। गोलोक त्रह्माण्डसे बाहर और ऊपर जानेपर उन्होंने बहुत-से आश्रम देखे, जो राधाकी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 4.8930)
- **Original**: है। उससे ऊपर दूसरा कोई लोक नहीं है। ऊपर प्रधान सस्ियोंके आवासस्थान थे। वे रूप, गुण,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 4.8931)
- **Original**: सब कुछ शून्य ही है। वहाँतक सृष्टिकी अन्तिम बेष, यौवन, सौभाग्य और अवस्थामें एक-दूसरीके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 4.8932)
- **Original**: सीमा है। सात रसातलोंसे भी नीचे सृष्टि नहीं समान थीं। श्रीराधाकी समवयस्का सखियाँ तैंतीस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 4.8933)
- **Original**: है, रसातलोंसे नीचे जल और अन्धकार है, जो गोपियाँ हैं, जिनकी वेशभूषा अनिर्वचनीय है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 4.8934)
- **Original**: अगम्य और अदृश्य है। (अध्याय 4) 3000“ *#ग्फ 422... श्रीराधाके विशाल भवन एवं अन्तःपुरकी शोभाका वर्णन, ब्रह्मा आदिको दिव्य तेजःपुझके दर्शन तथा उनके द्वारा उन तेजोमय परमेश्वरकी स्तुति भगवान्‌ नारायण कहते हैं--सम्पूर्ण
- **Translation**: 

---

### Verse 9 (Vaivtpuran 4.8935)
- **Original**: अलंकृत उस अद्भुत एवं विचित्र द्वारकी रक्षा गोलोकका दर्शन करके उन तीनों देवताओंके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 4.8936)
- **Original**: करते हुए द्वारपाल वीरभानुके पास जा देवताओंने मनमें बड़ा हर्ष हुआ। जे फिर श्रीराधाके प्रधान
- **Translation**: 

---

### Verse 11 (Vaivtpuran 4.8937)
- **Original**: प्रसन्नतापूर्वक्क अपना सारा अभिप्राय निवेदन द्वारपर आये। उस द्वारका निर्माण उत्तम रत्नों और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 4.8938)
- **Original**: किया। तब द्वारपालने निःशंक होकर उन मणियोंसे हुआ था। वहाँ दो वेदिकाएँ थीं।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 4.8939)
- **Original**: देवेश्वरॉंसे कहा-'देवगण! मैं इस समय आज्ञा हल्दीके रंगकी उत्तम मणिसे, जिसमें हौरेका भी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 4.8940)
- **Original**: लिये बिना आपलोगोंको भीतर नहीं जाने दूँगा'। सम्मिश्रण था, बनाये गये श्रेष्ठ रत्न-मणिनिर्मित)। मुने! यह कहकर द्वारपालने श्रीकृष्णके किवाड़ उस द्वारकी शोभा बढ़ाते थे। देवताओंने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 4.8941)
- **Original**: स्थानपर सेवकोंकों भेजा और उनकी आज्ञा पाकर देखा, उस द्वारपर रक्षाके लिये परम उत्तम
- **Translation**: 

---

### Verse 16 (Vaivtpuran 4.8942)
- **Original**: देवताओंकों अंदर जानेकी अनुमति दी। उससे वीरभानुकी नियुक्ति हुई है। वे रत्रोंक बने हुए
- **Translation**: 

---

### Verse 17 (Vaivtpuran 4.8943)
- **Original**: पूछकर वे तीनों देवता दूसरे उत्तम द्वारपर गये, सिंहासनपर बैठे हैं, पीताम्बर पहने हैं तथा रत्रमय
- **Translation**: 

---

### Verse 18 (Vaivtpuran 4.8944)
- **Original**: जो पहलेसे अधिक विचित्र, सुन्दर और मनोहर आधभूषणोंसे विभूषित हैं। उनके मस्तकपर रत्रमय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 4.8945)
- **Original**: था। नारद! उस द्वारपर नियुक्त हुए चन्द्रभानु मुकुट उद्धासित हो रहा है। विचित्र चित्रोंसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 4.8946)
- **Original**: नामक द्वारपाल दिखायी दिये, जिनकी अवस्था
- **Translation**: 

---

