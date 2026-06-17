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

### Verse 1 (Vishnu Puran 0.11421)
- **Original**: 12 श्रीपराझर उत्ाच इत्युक्तेडपगते दूते संस्मृत्याभ्यागतं हरि: । गम्नानम थारहा व्वरितिमतत्पा ययी
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11422)
- **Original**: 73 सम्पूर्ण देवणणको जोतकर महान्‌ कर्म किये थे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11423)
- **Original**: वह मैं सुन चुका ]
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11424)
- **Original**: इनके सिवा देवताओंकी चेष्टाओऑका विघात करनेवाले उन्होंने और भी जो कर्म किये थे, हे महाभाग ! वे सब मुझे सुनाइये; मुझे उनके सुननेक्त्र बड़ा कुतृहल हो रहा है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11425)
- **Original**: श्रीपराइरजी बोले--हे बहाएं ! भगवानने मनुष्यावतार लेकर जिस प्रकार काशीपुरी जलायी थी वह मैं सुनाता हूँ, तुम ध्यान देकर सुनो
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11426)
- **Original**: पौण्ड्कवंशीय वासुदेव नामक एक राजाकों अज्ञानमोहित पुरुष “आप वासुदेवरूपसे पृथिवीपर अवतीर्ण हुए हैं' ऐसा कहकर स्तुति किया करते थे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11427)
- **Original**: अन्तमें वह भी यही मानने लगा कि ैं बासुदेवरूपसे पृथियोमें अवतीर्ण हुआ हूँ !' इस प्रकार आत्म-विस्मृत हो जानेसे उसने विष्णुभगवान्‌के समस्त चिह्न घारण कर लिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11428)
- **Original**: और महात्मा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11429)
- **Original**: कृष्णचद्धके पास यह सन्देश लेकर दूत भेजा कि “हे घूढ़ ! अपने बासुदेव नामको छोड़कर मेरे चक्र आदि सम्पूर्ण चिह्नोंको छोड़ दे और यदि तुझे जोबनकी इच्छम है तो मेरी शरणमें आ'
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11430)
- **Original**: दूतने जब इसी प्रकार कहा तो श्रीजनार्दन उससे हँसकर बोले--“ठीक है, मैं अपने चिह्न चक्रफो तेरे प्रति छोड़ैगा। है दूत ! मेरी ओससे तू पौण्डकसे जाकर यह कहना कि मैंने तेरे खावयक्य वास्तविक भाव समझ लिया है, तुझे जो करना हो सो कर
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11431)
- **Original**: मैं अपने चिह्द और वेष घारणकर तेरे नगरमें आकँगा ! और निस्सत्देह अपने चिह चक्रको तेरे ऊपर छोड़ेंगा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11432)
- **Original**: और तूने जो आज्ञा करते हुए ' आ' ऐसा कहा है सो मैं उसे भी अवज्ष्य पालन करूँगा और कल शीघ्र ही तेरे पास पहुँचूँगा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11433)
- **Original**: हे राजन्‌ ! तेरी द्ारणमें आकर मैं यही उपाय करूँगा जिससे फिर तुझसे मुझे कोई भय नरहे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11434)
- **Original**: ओपरादारजी बोले--्रीकृष्णचद्धके ऐसा कहुनेपर जब दूत चला गया तो भगवान्‌ स्मरण करते ही उपस्थित हुए. गरुडपर चढ़कर तरंत उसकी राजधानीकों चले
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11435)
- **Original**: आः् इंड ] ततस्तु केशबोद्योगं श्रुत्वा काशिपतिस्तदा । पक्षम अंश ड03 भगवानके आक्रमणका समाचार सुनकर काहीनरेदा सर्वसैन्यपरीवार: पार्षिणिग्राह उपाययौ:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11436)
- **Original**: भी उसका पृषश्नपोषक (सहायक) होकर अपनी सम्पूर्ण ततो बलेन महता काशिराजबलेन च। पौण्ड्को वासुदेवोउसौ केशवाभिमुखो ययौ
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11437)
- **Original**: 15 ते ददर्श हरिरदूरादुदारस्यन्दने स्थितम्‌। चक्रहस्त॑ गदाशाईबाहुँ पाणिगताम्बुजम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11438)
- **Original**: 16 स्रग्धरं पीतवसने सुपर्णरचितध्वजम्‌। बक्ष:स्थल्े कृतं चास्य श्रीवत्सं ददृशे हरि:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11439)
- **Original**: 17 किरीटकुण्डलथरं॑ नानारत्रोपश्ोभितम्‌ । त॑ दृष्ठा भावगम्भीर॑ जहास गरुडध्वज:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11440)
- **Original**: 18 युबुधे के बलेनास्य हस्त्यश्रयलिना द्विज
- **Translation**: 

---

