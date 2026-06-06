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

### Verse 1 (Vishnu Puran 0.12641)
- **Original**: श्रीपराशरजी बोले--तब स्व्वाण्डिक्यने फिर अपने मन्लियोंसे परामर्श किया कि “यह मुझे गुरु-दक्षिणा देना चाहता है, मैं इससे क्या माँगूँ ?'”
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12642)
- **Original**: मन्लियोनि कहा--'“आप इससे सम्पूर्ण राज्य माँग लीजिये, बुद्धिमान्‌ लोग रात्रुऑसे अपने सैनिकॉको कष्ट दिये बिना राज्य ही माँगा करते हैं''
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12643)
- **Original**: तन महामति राजा खाण्डिक्यने उनसे हँसते हुए कहा---'' मेरे-जैसे लोग कुछ ही दिन रहनेवाला राज्यपद कैसे माँग सकते हैं ?
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12644)
- **Original**: यह ठौक है आपलोग स्वार्थ-साधनके लिये ही परामर्श देनेवाले हैं; किन्तु 'परमार्थ क्या और कैसा है ?' इस विषयमें आपको विशेष ज्ञान नहीं है”
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12645)
- **Original**: ओऔपराशरजी बोले--यह कहकर राजा खाण्डिक्य केशिध्वजके पास आये और उनसे कहा, “क्या तुम मुझे अखश्य गुरु-दक्षिणा दोगे ?'
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12646)
- **Original**: जब केशिध्वजने कहा कि “मैं अवदय दूँगा' तो स्ाण्डिक्य बोले---“आप आध्यात्मज्ञानरूप परमार्थ-विद्यामें बड़े कुशल हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12647)
- **Original**: सो यदि आप मुझे गुरु-दक्षिणा देना ही चाहते हैं तो जो कर्म समस्त फ्लेशॉकी झान्ति करनेमें समर्थ हो यह तत्क्ेशप्रशभायालं. यत्कर्म तदुदीर॒य
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12648)
- **Original**: बतलाइये'
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12649)
- **Original**: अैब----न__- कई वा इति श्रीविष्णुपुराणे षष्टेंडशे षष्टोउध्याय:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12650)
- **Original**: नमन जौ नन्‍न्‍्मजूूा, सातवाँ अध्याय ब्रह्मयोगका निर्णय केशिध्यज उकाच नप्नार्थित त्वया कस्मादस्मद्राज्यमकण्टकम्‌ । केशिध्वज खोल्ले--क्षत्रियोंको तो राज्य-प्राप्तिसे अधिक प्रिय और कुछ भी नहीं होता, फिर तुमने मेरा राज्यलाभाद्विना नान्यक्क्षत्रियाणामतिप्रियम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12651)
- **Original**: निष्कण्टक राज्य क्यों नहीं माँगा ?
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12652)
- **Original**: ख्राण्डिक्य उवाच केशिध्वज निबोध त्वं मया न प्रार्थितं यतः । खाण्डिक्य बोले--हे केशिध्वज ! मैंने जिस कारणसे तुम्हारा राज्य नहीं माँगा वह सुनो । इन राज्यादिकी राज्यमेतदशेष ते यत्र गृश्नन्त्यपण्डिता:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12653)
- **Original**: 2 आकाझ्ल तो मू्खोक्रे हुआ करती है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12654)
- **Original**: क्षत्रियाणामय धर्मों यत्मजापरिपालनम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12655)
- **Original**: क्षत्रियोंका धर्म तो यही है कि प्रजाका पालन करें और वथश्न धर्मयुद्धेन स्वराज्यपरिपन्थिनाम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12656)
- **Original**: अपने राज्यके विरेधियोंका घर्म-युद्धसे वध करें
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12657)
- **Original**: अ>7 ) घ्ठ अं अश्7 ) वंश छः र्थद9 तत्राश्क्तस्थ मे दोषों नैवास्त्थपद्ठते त्वया। शाक्तिहीन होनेके कारण यदि तुमने मेरा राज्य हरण कर बन्धायैव भवत्येषा हाविद्याप्यक्रमोज्झिता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12658)
- **Original**: लिया है, तो ( असमर्थताबश प्रजापाल्न न करनेपर जन्मोपभोगलिप्सार्थमियं राज्यस्पृह्टा मम । अन्येषां दोषजा सैब धर्म लै नानुरुध्यते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12659)
- **Original**: 5 न याच्आ क्षत्रबन्धूनां धमायितत्सतां मतम्‌ । अतो न याचितं राज्यमविद्यान्तर्गत तब
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12660)
- **Original**: 6 राज्ये गृश्नन्त्यविद्वांसो ममत्वाइतचेतस:। अहँमानमहापानमदमत्ता न मादृशा:
- **Translation**: 

---

