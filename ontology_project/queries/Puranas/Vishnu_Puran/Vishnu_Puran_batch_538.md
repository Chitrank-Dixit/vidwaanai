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

### Verse 1 (Vishnu Puran 0.10741)
- **Original**: 15 पिता माता तथा भ्राता भर्ता बन्धुजनश्र किम्‌ । सन्त्यक्तस्तत्कृतेरस्माभिरकृतज्ञध्वजो हि सः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10742)
- **Original**: 16 तथापि कब्चिदालापमिहागमनसंभ्रयम्‌ । करोति कृष्णों वक्तव्य भजता राम नानृतम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10743)
- **Original**: 97 दामोदरोउसौ गोविन्दः पुरख्रीसक्तमानस: । अपेतप्रीतिरस्मासु दुर्दर्शः प्रतिभाति नः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10744)
- **Original**: 18 अ्रीफाहर उवान् आमन्त्रितश्ष॒ कृष्णेति पुनर्दामोदरेलि ऋ। जहसुस्सस्वर॑गोप्यो हरिणा इतचेतस:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10745)
- **Original**: 19 सन्देशैस्साममधुरैः प्रेमगर्भैरगर्लिति: । रामेणाश्वासिता गोप्य: कृष्णस्थातिम्नोहरैः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10746)
- **Original**: 20 गोपैश पूर्वबद्रामः परिहासमनोहरा: । करते ?
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10747)
- **Original**: क्‍या कृष्णचन्द्र कभी हमारे गीतानुयायी मनोहर स्वरका स्मरण करते हैं ? क्‍या ये एक यार अपनी माताको भो देखनके लिये यहाँ आलेंगे ?
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10748)
- **Original**: अथवा अब उनकी बात करनेसे हमें क्या प्रयोजन है, कोई और बात करो । जब उनकी हमारे बिना निभ गयी तो हस भी उनके बिना निभा ही लेंगी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10749)
- **Original**: क्‍या माता, क्या पिता, क्या बच्चु, क्या पति और क्या कुटुम्बके ल्थेग ? हमने उनके छिये सभीको छोड़ दिया, किन्तु वे तो अकृतज्ञॉफी ध्यजा ही निकले
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10750)
- **Original**: तथापि अल्समजी ! सच-सच बतलाइये क्या कृष्ण कभी यहाँ आगेके बिषयमें भी कोई बातचीत करते >
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10751)
- **Original**: हमें ऐसा प्रतीत होता ऐ कि दामोदर कृष्णका छित्त नागरी-नारियोंमें फैंस गया है; हममें अब उनकी प्रीति नहीं है, अतः अब रमें तो ठनका दर्शन दुर्लभ ही जान पड़ता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10752)
- **Original**: श्रीपराहरजी खोल्ले--तदनन्तर श्रीहरिने जिनका चित्त हर लिया है वे गोपियाँ बलछरागजीको कृष्ण और दामोदर कहकर सम्बोधन करने लगीं और फिर उच स्वस्से हँसने रूपों
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10753)
- **Original**: तब बलभद्रजीने कृष्णचद्धका अति मनोहर और शाक्तिमय, प्रेमगर्भित और गर्वहीन सन्देश सुनाकर गोपियोंको सान्त्वना दी
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10754)
- **Original**: तथा गोपोंके साथ हास्य करते हुए उन्होंने पहलेकी भाँति अहुत-सी मनोहर बातें कीं और उनके साथ ब्रजभूमिमें नाना प्रकास्की कथाक्षकार रेमे च सह तेत्रजमूमिषु
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10755)
- **Original**: ल्लीलाएँ करते रहे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10756)
- **Original**: का जी चतचत इति श्रीविष्णुपुराणे पश्षमेंउद्ञों चतुर्विशोउध्याय:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10757)
- **Original**: च्च्च्स् कर सल्‍वचक पचीसवाँ अध्याय खर्ूभड्रजीका ख्रज-विहार तथा यप्तुनाकर्षण श्रीपराशर उवाच बने क्िचिरतस्तस्थ सह गोपैर्महात्मन: । मानुषच्छडारूपस्थ शोषस्थ धरणीधृत:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10758)
- **Original**: *1 निष्पादितोरुकार्यस्य कार्येणोवीग्रचारिण: । उपभोगार्थमत्यर्थ बरुण: प्राह वारुणीम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10759)
- **Original**: 2 अभीष्टा सर्वदा यस्य पदिरे त्व॑ं महोजस: । अनन्तस्योपभोगाय तस्थ गच्छ मुदे शुभे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10760)
- **Original**: 3 इत्युक्ता वारुणी तेन सन्निधानमथधाकरोत्‌ । वृन्दावनसमुत्पन्नकटम्बतरुकोटरे
- **Translation**: 

---

