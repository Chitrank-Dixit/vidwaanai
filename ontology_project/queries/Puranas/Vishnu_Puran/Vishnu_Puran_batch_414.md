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

### Verse 1 (Vishnu Puran 0.8261)
- **Original**: अप्रतिरथका टूसरा पुत्र ऐलोन था
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8262)
- **Original**: इस ऐलीनके दुष्यन्त आदि चार पुत्र हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8263)
- **Original**: दुष्यत्तके यहाँ चक्रवर्ती सम्राट्‌ भरतका जन्म हूआ जिसके नामके बिषयमें देवगणने इस इत्मेकका गान किया था-
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8264)
- **Original**: “माता तो केबल चमड़ेकी धौंकनीके समान है, पुत्रपर अधिकार तो पिताका ही है, पुत्र जिसके द्वारा जन्म ग्रहण करता है उसीका स्वरूप होता है। हे दुष्यन्त ! तू इस पुत्रका पालन-पोषण कर, शकुन्तलाका अप्रमान न कर
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8265)
- **Original**: हे नरदेव ! अपने ही बीर्यसे उत्पन्न हुआ पुत्र अपने पिताको यमल्मेकसे [ उद्धार कर स्वर्गत्त्रेकको ] ले जाता है। 'इस पुषत्रके आधान करनेवाले तुम्हों हो-- दाकुन्तल्ाने यह बात ठीक ही कही है"
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8266)
- **Original**: भरतके तीन ख्ियाँ थीं जिनसे उनके नौ पुत्र हुए
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8267)
- **Original**: भरतके यह कहनेपर कि, 'ये मेंरे अनुरूप नहीं हैं', उनकी माताओने इस भयसे कि, राजा हमको त्याग न दें, उन पुत्रॉको मार डाला
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8268)
- **Original**: इस प्रकार पुत्र-जन्मके विफल हो जानेसे भरतने पुत्रकी कामनासे मरूसोम नामक यज्ञ किया। उस यज्ञके अन्तमें मरुद्रणने उन्हें भरदाज नामक एक बालक पुन्ररूपरो दिया जो उत्तथ्यपत्नी ममताके
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8269)
- **Original**: 290 तस्यापि नामनिर्वत्ननइलोक: पठ्यते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8270)
- **Original**: मूढे भर द्वाजमिम भर द्वाजं बृहस्पते। यातौ यदुकत्वा पितरी भरद्वाजस्ततस्त्वयम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8271)
- **Original**: 18 भरद्वाजस्स वितथे पुत्रजन्यनि मरुद्धिर्दत्तस्ततो वितथसंज्ञामबाप
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8272)
- **Original**: वितश्रस्थापि मन्यु: पुत्रोहभत्त्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8273)
- **Original**: बृहत्क्षत्रमहावीर्यनरगर्गा अभवन्मन्युपुत्रा:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8274)
- **Original**: नरस्य सड्कृतिस्सक्कृते- गुरुप्रीतिरन्तिदेवों
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8275)
- **Original**: गर्गाच्छिनि ततश्च॒गार्ग्याइशैन्या: क्षत्रोपेता द्विजातयो खभूयु:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8276)
- **Original**: महावीर्याध् दुरुक्षयो नाम पुत्रो>भबत्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8277)
- **Original**: तस्य त्रय्यारुणि: पुष्करिण्यो कपिश्न पुत्रयमभूत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8278)
- **Original**: तथ पुत्रत्रितयमपि पश्चाद्रिप्रतामुपजगाम
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8279)
- **Original**: . बृहत्क्षत्रस्य सुद्दोन्र:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8280)
- **Original**: सुहोत्राद्धस्ती य इदं हस्तिनापुर- मायासयामास
- **Translation**: 

---

