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

### Verse 1 (Markende Puran 0.1621)
- **Original**: स्वागत-सत्कार किया। बातचीतके प्रश्नकग अभ्यागतने प्रार्केण्डेयजीने कहा --मुगे। मैंने तमहें स्त्ायम्भुत ; ब्रह्मससे अनेकों देशों, रमणीय नाएं, वनों, नदियों, पमजव्तरकी बातें तो बता दीं अब स्वागेनिप नामक
- **Translation**: 

---

### Verse 2 (Markende Puran 0.1622)
- **Original**: पर्वतों और परुण्यतीर्थोकों बातें बतायों। यह सच दूसरे मन्‍्बन्तरका दर्णन सुनो। वरुणा नदीके तटपर
- **Translation**: 

---

### Verse 3 (Markende Puran 0.1623)
- **Original**: श्रुनकरब्राह्मणकों बड़ा विस्मय हुआ। वे अरुणाझूमद नामक नाएमें एक श्रेष्ठ ब्राह्मण रहते
- **Translation**: 

---

### Verse 4 (Markende Puran 0.1624)
- **Original**: बोले--'तरिप्रवर! आपने अनेक देश देखनेके कारण थे। उनका रूप अश्विनीकुमारोंके समान मनोहर था।
- **Translation**: 

---

### Verse 5 (Markende Puran 0.1625)
- **Original**: बहुत परिश्रम उठाया है तो भी न तो आप अल््न्त वे स्वभावसे मृदु, सदाचारी तथा वेद-वेदाज्ञोंके
- **Translation**: 

---

### Verse 6 (Markende Puran 0.1626)
- **Original**: बृढ़ें हुए और न जवानीने ही आपका साथ छोड़ा। यारणामी थे। अतिथियोंके प्रति उनका सदा ही प्रेम
- **Translation**: 

---

### Verse 7 (Markende Puran 0.1627)
- **Original**: थोड़े ही समयमें आप सारी पृध्वीपर कैसे भ्रपण अना रहता था। ग़तकों घरपर आबे हुए अभ्यागतोंको
- **Translation**: 

---

### Verse 8 (Markende Puran 0.1628)
- **Original**: कर लेते हैं?" के उहरनेके लिंवे स्थान देते और उनके भोजन
- **Translation**: 

---

### Verse 9 (Markende Puran 0.1629)
- **Original**: आगगमन्तुक ब्वाह्मणने ऋह्ा--' ब्हमन्‌! सन्त्र आदिकी भी व्यवस्था करते थे। उनके पनपें प्राय:
- **Translation**: 

---

### Verse 10 (Markende Puran 0.1630)
- **Original**: और ओपधियोंके प्रभावसे मेरी गति रहीं भी यई विचार उठा कर्ता था कि मै स्मणीव छून,
- **Translation**: 

---

### Verse 11 (Markende Puran 0.1631)
- **Original**: नहीं रुकती। गैँ आधे दिनमें एक हजार योजन उद्यान एथा भौएि- भौतिके नगरोंसे सुशोभित सम्पूर्ण
- **Translation**: 

---

### Verse 12 (Markende Puran 0.1632)
- **Original**: चलता हूँ।
- **Translation**: 

---

### Verse 13 (Markende Puran 0.1633)
- **Original**: 146 «संड्िषति स्यर्कण्डेयप्राण ऋफाज 2 #क + 3 आल है हुआ: कु डुऊ-
- **Translation**: 

---

### Verse 14 (Markende Puran 0.1634)
- **Original**: कुक + 2ऋआंन शऊू- 0 जअक _3.2560 0 3.0 सु5.240 227 /4 02334, 7 5 /जउ' 33 4 अल । हहते थे। किन्नरगण बिहार करते थे तथा इधर
- **Translation**: 

---

### Verse 15 (Markende Puran 0.1635)
- **Original**: धर देखता आदिके क्री्धा-विहारसे वहाँको
- **Translation**: 

---

### Verse 16 (Markende Puran 0.1636)
- **Original**: स्पणीयठा जहुत बढ गयो थी। सैकड़ों टिव्य । अप्पराओंधे भो हुए कहाँके मनोहर शिखरोंका दर्शन करनेसे ब्राह्मणदेवताफों तृप्ति नहाँ हुई।
- **Translation**: 

---

### Verse 17 (Markende Puran 0.1637)
- **Original**: उनके शरौरमें रोम! हो आया।
- **Translation**: 

---

### Verse 18 (Markende Puran 0.1638)
- **Original**: . फिर दूसरे द्वित आतेका विचार करके जय वे कर जानेको उद्यत हुए तो उन्हें अपने चैरोंकी गति कुण्टित जान पड़ी। बे सोचने लगे-
- **Translation**: 

---

### Verse 19 (Markende Puran 0.1639)
- **Original**: ' अहो! यहाँ बर्फत्के पादोसे मेरे पैरका लेप धुल
- **Translation**: 

---

### Verse 20 (Markende Puran 0.1640)
- **Original**: हया। इधर यह पर्वत अत्यस दुर्गंप है और में
- **Translation**: 

---

