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

### Verse 1 (Vishnu Puran 0.7021)
- **Original**: तत्कर्मकर्तुत्व॑च गौतमस्य दृष्ठा स्वपते तस्मै राज्ञे मां प्रत्याख्यायैतदनेन गौतमाय कर्मान्तरं समर्पित यस्मात्तस्मादयं विदेहो भविष्यतीति शाप॑ ददौ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7022)
- **Original**: प्रबुद्धआसाववनि- पतिरपि प्राह
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7023)
- **Original**: यस्मान्याससम्धाष्या- ज्ञानत एवं शयानस्य शापोत्सर्गमसौ दुष्टगुरुश्ककार तस्मात्तस्यापि देह: पतिष्यतीति ज्ञापं द्त्त्वा देहमत्यजत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7024)
- **Original**: तच्छापाच्च मित्रावरुणयोस्तेजसि बसिष्ठस्य चेत प्रविष्टम
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7025)
- **Original**: उर्वशीदर्शनादुद्धूत बीजप्रपातयोस्तयोस्सकाशाहसिप्ठो.. देहमपरं लेभे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7026)
- **Original**: दोषमवाप सद्यो मृत डब तस्थौ
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7027)
- **Original**: यज्ञसमाप्तौ भागग्रहणाय देवानागतानृत्विज ऊचुर्यजमानाय बरो दीयतामिति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7028)
- **Original**: देवैशञ छन्दितोउसौ निमिराह
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7029)
- **Original**: भगवन्‍्तो5खिल- संसारदुःखहन्तार:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7030)
- **Original**: न होतादूगन्यद्‌- दुःसखमस्ति यच्छरीरात्मनोर्वियोगे भवति
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7031)
- **Original**: तदहमिच्छामि सकलल्ोकल्लोचनेषु वस्तु न पुनइ्शरीरप्रहणं. कर्तुमित्येवमुक्तैदेंवेरसावशेष- श्रीपराशरजी बोले--शक्ष्वाकुका जो निमि नामक पुत्र था उसने एक सहस्रवर्षमें समाप्त होनेवाले यज्ञका आरण्य कियो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7032)
- **Original**: उस यजञमें उसने वसिप्तजीको होता वरण किया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7033)
- **Original**: बसि्ठजीने उससे कहा कि पाँच सौ वर्षके यज्ञके लिये इन्द्रने मुझे पहले ही बरण कर लिया है।
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7034)
- **Original**: अतः इतने समय तुम ठहर जाओ, बहाँसे आनेपर मैं तुम्हारा भी ऋत्विक्‌ हो जाऊँगा। डनके ऐसा कहनेपर राजाने उन्हें कुछ भी उत्तर नहीं दिया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7035)
- **Original**: बसिश्ठदजीने यह समझकर कि राजाने उनका कथन स्वीकार कर लिया है इन्द्रका यज्ञ आरण्प कर दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7036)
- **Original**: कितु राजा निमि भी उसी समय अन्य ज्ोताओंद्वारा अपना यज्ञ करने ल्मो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7037)
- **Original**: देखराज इन्रका यज्ञ समाप्त होते ही “मुझे निमिका यज्ञ कराना है' इस खिचारसे वसिष्ठज़ी भी तुरैत ही आ गये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7038)
- **Original**: उस यह्ञमें अपना [झोताका) कर्म गौतमकों करते देख उन्होंने सोते हुए राजा निभिको यह शाप दिया कि “इसने मेरी अवज्ञा करके सम्पूर्ण कर्मफा भार गौतमको सौंपा है इसलिये यह देहहीन हो जायगा'
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7039)
- **Original**: सोकर उठनेपर राजा निमिने भी कहा--
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7040)
- **Original**: “इस दुष्ट गुरुने मुझसे बिना बातचीत किये अज्ञानतापूर्वक मुझ सोये हुएको ज्ञाप दिया है, इसलिये इसका देह भी नष्ट हो जायगा।” इस अऋ्रकार ज्ञाप देकर राजाने अपना दारीर छोड़ दिया
- **Translation**: 

---

