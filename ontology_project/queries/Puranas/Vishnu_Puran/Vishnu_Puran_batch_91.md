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

### Verse 1 (Vishnu Puran 0.1801)
- **Original**: 24 इत्युक्त: स तया प्राह परिवृत्तमह: शुभे। सम्ध्योपास्ति करिष्यामि क्रियाल्लोपोउन्यथा भवेत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1802)
- **Original**: ततः प्रहस्य सुदती ते सा प्राह महामुनिम्‌ । किमद्य. सर्वधर्मज्ञ॒ परिवृत्तमहस्तव
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1803)
- **Original**: 26 बहूनां विप्र वर्षाणां परिवृत्तमहस्तव । गतमेतन्न॑ कुरुते विस्मयं कस्य कथ्यताम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1804)
- **Original**: 27 मुत्रित्वाच प्रातस्त्वमागता भट्ठे नदीतीरमिद शुभम्‌। मया दृष्टासि तन्व्लि प्रविष्टास ममाश्रमम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1805)
- **Original**: 28 इये तर वर्तते सन्ध्या परिणाममहर्गतम्‌। अपहास: किमर्थो5यं सद्धाव: कथ्यतां मप्र
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1806)
- **Original**: 29 अस्त्मेक्षोवात्त प्रत्यूषस्यागता क्रह्मन्‌ सत्यमेतन्न तन्म्रृषा । नन्वस्य तस्य कालस्य गतान्यब्दशतानि ते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1807)
- **Original**: 30 सोम उबाच ततस्ससाध्वसो विश्रस्तां पप्रच्छायतेक्षणाम्‌ । कथ्यतां भीरु क: कालस्त्वया मे रमत: सह
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1808)
- **Original**: 31 प्रस्लोचोवाच सप्तोत्तराण्यतीतानि नववर्षशतानि ते। मासाश्च षदतथैवान्यत्समतीतं दिनत्रयम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1809)
- **Original**: 32 ऋषिस्वाच सत्यं भीरु वदस्येतत्यरिहासोड्थ वा शुभे । देवल्नेककों जानेके लिये कहती तभी-तभी कप्डु ऋषि उससे यही कहते कि 'अभी ठहर जा'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1810)
- **Original**: मुनिके इस प्रकार कहनेपर, प्रणयर्भंगकी पीड़ाको जाननेवाली उस दक्षिणाने * अपने दाक्षिण्यवद् तथा मुनिके झापसे भयभीत होकर उन्हें न छोड़ा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1811)
- **Original**: तथा उन महर्षि महोदयक्रा भी, कामासक्तचित्तसे उसके साथ अहर्तिश रमण करते-करते, उसमें नित्य नूतन प्रेम बढ़ता गया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1812)
- **Original**: एक दिन ले मुनिवर बड़ी शीघ्रतासे अपनी कुटीसे निकले। उनके निकलते समय वह सुन्दरी बोलौ-- “आप कहाँ जाते हैं”
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1813)
- **Original**: उसके इस प्रकार पूछनेपर मुनिने कहा--''हे झरुभे ! दिन अस्त हो चुका है, इसलिये मैं सम्ध्योपासना करूँगा; नहीं तो नित्य-क्रिया नष्ट हो जायगी"
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1814)
- **Original**: तब उस सुन्दर दाँतोंवालीने उन मुनीधरसे हैंसकर कहा--“'हे सर्वरर्मज्ञ ! क्या आज ही आपका दिन अस्त हुआ है ?
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1815)
- **Original**: हे विप्र ! अनेकों वर्षकि पश्चात्‌ आज आपका दिन अस्त हुआ है; इससे कहिये, किसको आश्चर्य न होगा ?'
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1816)
- **Original**: मुनि बोले--भट्रे ! नदीके इस सुन्दर तटपर तुम आज सबेरें ही तो आयी हो। [ मुझे भली प्रकार स्मरण है ] मैंने आज ही तुमको अपने आश्रममें प्रवेश करते देखा था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1817)
- **Original**: अब दिनके समाप्त होनेपर यह सख्याकाऊ हुआ है। फिर, सच तो कहो, ऐसा डपहास क्‍यों करती हो ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1818)
- **Original**: प्रम्लोच्ा जोली--अहान्‌ ! आपका यह कथन कि “तुप्त सबेरे ही आयी हो' ठोक ही है, इसमें झूठ नहीं; परन्तु उस्र समयको तो आज सैकड़ों वर्ष बीत चुके
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1819)
- **Original**: सोमने कहा--तब उन विप्रबरने उस विद्याव्पक्षीसे कुछ घबड़ाकर पूछा--''अरी भीरु ! ठझीक-टीक बता, तेरे साथ रमण करते मुझे कितना समय बोत गया 2”
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1820)
- **Original**: ब्रम्लोचाने कहा--अखतक नौ सौ सात बर्ष, छः महीने तथा तीन दिन और भी बीत चुके हैं
- **Translation**: 

---

