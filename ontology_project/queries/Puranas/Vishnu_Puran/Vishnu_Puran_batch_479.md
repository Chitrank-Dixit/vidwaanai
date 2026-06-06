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

### Verse 1 (Vishnu Puran 0.9561)
- **Original**: अतः है अगेयात्मन्‌! आप अपने स्वरूपको स्मरण कॉजिये और मनुष्यभावका ही अबल्म्बनकर इस दैत्यको मारकर बन्धुजनोंका हित- स्वधन कीजिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9562)
- **Original**: श्रीपरावारजी बोले--है चिप्र! महात्मा कृष्णचन्द्रहराा इस प्रकार स्मरण कराये जानेपर सहाबलबान्‌ बछरामजी हँसते हुए प्रलूम्बासुरको पीड़ित करने लगे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9563)
- **Original**: उन्होंने से नेत्र लाल करके उसके मस्तकपर एक घूँसा मारा, जिसकी चोटसे उस दैत्यके दोनों नेत्र बाहर निकल आये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9564)
- **Original**: आ* 10 ] पञ्मम अंश 335 स्‌ निष्कासितमस्तिष्कों मुखाच्छोणितमुद्रमन्‌ । निपपात महीपूृष्ठे दैत्यवयों मार च्
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9565)
- **Original**: 36 प्रकतम्य॑ निहते दृष्ठा बलेनाद्भधुतकर्मणा प्रहष्टास्तुष्ठतुरगोपास्साधुसाध्विति चाब्रुबन्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9566)
- **Original**: 37 गोपैस्तु रामो दैत्ये निपातिते। अ्रछलम्ये सह कृष्णेन पुनर्गोकुलमाययौं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9567)
- **Original**: 38 तदनन्तर वह दैत्यश्रेष्ठ मगज (मस्तिष्क) फट जानेपर मुखसे रक्त वमन करता हुआ यृथिवीपर गिर पड़ा और मर गया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9568)
- **Original**: अच्धुत्तकर्मा बल्गमजीद्वारा प्ररूम्बासुरको मरा हुआ देखकर गोपगण प्रसन्न होकर “साधु, साधु कहते हुए उनकी प्रशंसा करने छगे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9569)
- **Original**: प्ररूप्बासुरके मारे जानेपर बलरशमजी गोपोंद्वारा प्रशंसित होते हुए, कृष्णचच्धके साथ गोकुलमें त्जैट आये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9570)
- **Original**: इति श्रीनिष्णुपुराणे पञ्ञमेंउशे नवमोड्थ्यायः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9571)
- **Original**: न छा दसवाँ अध्याय झरद्वर्णन तथा गोवर्धनकी पूजा ओपयरार उकाच तयोर्विहरतोरेवं रामकेशवयोद्तरजे । प्रावृद् व्यतीता विकसत्सरोजा चाभवच्छरत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9572)
- **Original**: 9 अबापुस्तापमत्यर्थ शफर्य: पल्‍्वलोदके । पुत्रक्षेत्रादिसक्तेन ममत्वेन यथा गृही
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9573)
- **Original**: 2 मयूरा मौनमातस्थुः परित्यक्तमदा बने। असारतां परिज्ञाय संसारस्येव योगिन:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9574)
- **Original**: 3 उत्सृज्य जलसर्वस्व॑विमलास्सितमूर्त्तय: । तत्यजुश्चाप्बरं मेघा गृह विज्ञानिनो यथा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9575)
- **Original**: 4 शरत्सूयौशुतप्तानि ययुइ्शोष॑ सरांसि “च
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9576)
- **Original**: बड्लालम्बममत्वेन हृदयानीव देहिनामू
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9577)
- **Original**: 5 कुमुदैदशरदप्भांसि योग्यतालक्षणं ययु: । अवबोधैर्मनांसीव. समत्वममलात्मनाम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9578)
- **Original**: 6 तारकाबिमले व्योप्नि रराजाखण्डप्रण्डल: । चन्धशक्षरमदेहात्मा योगी साधुकुले यथा ।
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9579)
- **Original**: 7 शनकैइ्शनकैस्तीरं तत्यजुश्न जलाशया:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9580)
- **Original**: ममत्व क्षेत्रपुत्रादिसूठमुचैर्यथा बुधा:
- **Translation**: 

---

