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

### Verse 1 (Narsihma Puran 0.1141)
- **Original**: पद्मादनुपर्ण:। अनुपर्णाद्वस्त्रपाणि:
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.1142)
- **Original**: बस्त्रपाणे: शुद्धोदन:। शुद्धोदनाद्वुध:
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.1143)
- **Original**: बुधादादित्यवंशो निवर्तते
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.1144)
- **Original**: सूर्यबंशभवा ये ते प्राथान्येन प्रकीर्तिता:। यैरियं पृथिवी भुक्ता धर्मतः क्षत्रिय: पुरा
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.1145)
- **Original**: 16 सूर्यस्थ वंश: कथितो मया मुने समुद्वता यत्र नरेश्वरा: पुरा। मयोच्यमानाउछशित:. सम्राहितः श्रृणुष्व बंशे5थ नृपाननुत्तमान्‌
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.1146)
- **Original**: 17 श्रीनरसिंहपुराण
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.1147)
- **Original**: अध्याय 22 आदी ताबदुह्मा ब्रह्मणो मरीचि:
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.1148)
- **Original**: मरीचे: कश्यप: सबसे पहले ब्रह्माजो प्रकट हुए; उनसे मरोचि, मरीचिसे कश्यप, कश्यपसे सूर्य, सूर्यसे मनु, सनुसे इक्ष्वाकु, इक्ष्वाकुसे विकुक्षि, विकुक्षिसे ोत, झ्ोतसे येन, पेनसे पृथु और प्रथुसे पृथाश्रकों उत्पत्ति हुई। पृथाश्वसे असंख्याताश्व, असंख्याताश्वसे मान्धाता, सान्धातासे पुरुकुत्स, पुरुकुत्ससे दृषद, दृघदसे अभिशम्भु, अभिशम्भुसे दारूण, दारुणसे सगर, सगरसे हर्यथ्र, हर्यश्वसे हारोत, हारीतसे रोहिता श्र, रोहिताश्रसे अंशुमान्‌ तथा अंशुमानूसे अगीरध उत्पन्न हुए। भगीरथसे सौदास, सौदाससे शब्रुंदम, शन्नुंदमसे अनरण्य, अनरण्यसे दीघंबाहु, दीर्घबाहुसे अज, अजसे दशरथ, दशरथसे श्रीराम, श्रीरामसे लव, लबसे पद्म, पद्मसे अनुपर्ण और अनुपर्णसे वस्त्रपाणिका जन्म हुआ। यस्त्रपाणिसे शुद्धोदद और शुद्धोदनसे बुध (युद्ध) की उत्पत्ति हुईं। बुधसे सूर्यबंश समाप्त हों जाता हैं
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.1149)
- **Original**: सूर्यवंशमें उत्पन्न हुए जो क्षत्रिय हैं, उनमेंसे मुख्य-मुख्य लोगोंका यहाँ वर्णन किया गया है, जिन्होंने पूर्वकालमें इस पृथ्वीका धर्मपूर्वक्व पालन किया है। मुने! यह मैंने सूर्यतंंशका वर्णन किया है, जिसमें प्राचीन कालमें अनेकानेक़ नरेश हो गये हैं। अब मेरे द्वारा अतलाये जानेवाले चद्रयंशोय परम उत्तम राज़ाओंका बर्णन आपलोग सुनें
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.1150)
- **Original**: इति ऑनरफिंहप्रद्मणे यूर्यवंशक्षथत फर्मेकर्विश्ेए ध्याय। 4 21 # उस प्रकार कैतराशिए्द्राणगें 'स॒र्वप्रशका यर्णत ' नासक उक्फोसवाँ अध्याय एस हुआ 21 4 हमर के #बतरा अन्धंशका वर्णन दुए उकात सोमवंश श्रृणुप्वाथ भरद्वाज महामुने। सूत्तजी बोले--महामुते भरदाज! अब चन्द्रवंशका यर्णन सुनो। (अन्य) पुराणोंमें इसका बिस्तारपूर्वक वर्णन पुराणे बिस्तरेणोक्त संक्षेपात्‌ कथये5धुना
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.1151)
- **Original**: किया गया है, अतः इस समय मैं यहाँ संक्षेपसे इसका आदौ तावद्ुह्य। बरह्मणो मानसः पुत्रो
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.1152)
- **Original**: वर्णन करता हूँ
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.1153)
- **Original**: परीचिर्मरीचेर्दाक्षायएयां कश्यप:
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.1154)
- **Original**: कश्यपा- सर्वप्रथम ग्रह्माजी हुए, उनके मानसपुत्र मरीचि हुए,
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.1155)
- **Original**: ददितेरादित्य: । आदित्यात्‌ सुवर्चलायां मनु:
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.1156)
- **Original**: म्नो: सुरूपायां सोम:। सोमाद्रोहिण्यां बुध:। बुधादिलायां पुरूरवा:
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.1157)
- **Original**: पुरूरवस आयु:। आयो रूपवत्यां नहुष:
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.1158)
- **Original**: नहुषात्‌ पितृवत्यां ययाति:। ययाते: शर्मिफ्ल॒यां पूरु:
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.1159)
- **Original**: पूरोर्वशदायां सम्पाति: । सम्पातेर्भानुदत्तायां सार्वभौम: । सार्वभौ मस्य बैदेह्वां भोज:
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.1160)
- **Original**: भोजस्य लिड्डायां दुष्यन्त: । दुष्यन्तस्य शकुन्तलायां भरत:
- **Translation**: 

---

