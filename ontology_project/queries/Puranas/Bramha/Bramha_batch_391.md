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

### Verse 1 (Bramha 0.7801)
- **Original**: है। हर एककों इसका उपदेश नहीं देना चाहिये। जो नास्तिक हो, जिसकी बुद्धि खोटी हो, जो दम्भी, मूर्ख और कुतर्कपूर्ण बा्तालाप करनेबवाला हो, ऐसे मनुष्यकों कदापि इसका उपदेश नहीं देना चाहिये। >> ्
- **Translation**: 

---

### Verse 2 (Bramha 0.7802)
- **Original**: *वर्ण और आश्रषोंके धर्मका निरूपण « 375 वर्ण और आश्रमोंके धर्मका निरूपण मुनियोंने कहा--ब्रह्मन्‌! अब हम वर्णधर्म
- **Translation**: 

---

### Verse 3 (Bramha 0.7803)
- **Original**: वेदोंका अध्ययन, यह्ष, दान, धर्म तथा नित्य और और आश्रमधर्मका विशेष रूपसे वर्णन सुनना
- **Translation**: 

---

### Verse 4 (Bramha 0.7804)
- **Original**: नैभित्तिक आदि कर्मांका अनुष्ठान बैश्यके लिये भी चाहते हैं। विप्रवर! अब उसीका वर्णन कीजिये।
- **Translation**: 

---

### Verse 5 (Bramha 0.7805)
- **Original**: उत्तम है। शुद्र द्विजातियोंकी सेवाका कार्य करे व्यासजी बोले-द्विजवरो! अब मैं क्रमशः
- **Translation**: 

---

### Verse 6 (Bramha 0.7806)
- **Original**: और उसीसे अर्थोंपार्जज करके अपना जीवन- ब्राह्मण, क्षत्रिय, वैश्य और शुद्र-इन चारों वर्णोंके
- **Translation**: 

---

### Verse 7 (Bramha 0.7807)
- **Original**: निर्वाह करे। अथवा खरीद-बिक्री या शिल्पकर्मके धर्मका वर्णन करूँगा। तुमलोग एकाग्रचित्त
- **Translation**: 

---

### Verse 8 (Bramha 0.7808)
- **Original**: द्वारा धन पैदा करके उससे जीविका चलाये। शूद्र होकर सुनो। ब्राह्मणको सदा दान, दया, तपस्या,
- **Translation**: 

---

### Verse 9 (Bramha 0.7809)
- **Original**: भी दान दे और मन्त्रहीन पाक-यक्ञोंद्वारा यजन देवयज्ञ और स्वाध्यायमें तत्पर रहना चाहिये।
- **Translation**: 

---

### Verse 10 (Bramha 0.7810)
- **Original**: करे। बह श्राद्ध आदि सब कार्य बिना मन्त्रके कर तर्पण और अग्रिहोत्र उसका प्रतिदिनका कार्य
- **Translation**: 

---

### Verse 11 (Bramha 0.7811)
- **Original**: सकता है। भृत्य आदिका भरण-पोषण करनेके होना चाहिये। जीविकाके लिये वह अन्य द्विजोंका
- **Translation**: 

---

### Verse 12 (Bramha 0.7812)
- **Original**: लिये सबके लिये संग्रह आवश्यक है। ऋतुकालके यज्ञ कराये तथा उन्हें पढ़ाये। यज्ञ करनेके लिये
- **Translation**: 

---

### Verse 13 (Bramha 0.7813)
- **Original**: समय अपनी पलीके पास जाना, सब प्राणियंकि वह जान-बूझकर भी प्रतिग्रह ले सकता है। सब
- **Translation**: 

---

### Verse 14 (Bramha 0.7814)
- **Original**: प्रति दयाभाव रखना, शीत, उष्ण आदि इन्द्ोंको लोगोंका हितसाधन करना और किसीका भी
- **Translation**: 

---

### Verse 15 (Bramha 0.7815)
- **Original**: सहन करना, अभिमान न रखना, सत्य बोलना, अपने द्वारा अहित न होने देना, यह ब्राह्मणका
- **Translation**: 

---

### Verse 16 (Bramha 0.7816)
- **Original**: पविश्रतापूर्वक्त रहना, किसीकों कष्ट न पहुँचाना, कर्तव्य है। समस्त प्राणियोंके प्रति मैत्रीका होना,
- **Translation**: 

---

### Verse 17 (Bramha 0.7817)
- **Original**: सबका मज्भल करना, प्रिय वचन बोलना, सबके यह ब्राह्मणके लिये सबसे उत्तम धन है।* केवल
- **Translation**: 

---

### Verse 18 (Bramha 0.7818)
- **Original**: प्रति मैत्रीका भाव रखना, किसी वस्तुकी कामना न पत्नोके साथ समागम करता ब्राह्मणके
- **Translation**: 

---

### Verse 19 (Bramha 0.7819)
- **Original**: करना, कृपणता न करना तथा किसीके भी दोष न लिये प्रशंसाकी बात है। क्षत्रिय भी अपने इच्छानुसार
- **Translation**: 

---

### Verse 20 (Bramha 0.7820)
- **Original**: देखना-ये सभी वर्णोंके लिये सामान्यरूपसे उत्तम ब्राह्मणको दान दे, नाता प्रकारके यज्ञोंद्रारा भगवानूका
- **Translation**: 

---

