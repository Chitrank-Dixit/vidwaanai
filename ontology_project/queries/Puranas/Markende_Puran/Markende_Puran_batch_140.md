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

### Verse 1 (Markende Puran 0.2781)
- **Original**: काप्मास्ते स्त्री महाराज भासयन्ती हिमाचलमू
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2782)
- **Original**: नैव तज्ञादृछ क्रचिद्वूर्प दृष्टे क्ेनचितुक्तमस्‌। ज्ञायतों काप्यसौ देवी गृद्यतां चासुरेश्वर
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2783)
- **Original**: स्त्रीरत्वमतिचार्वज्री द्योतवन्ती दिशस्त्विषा
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2784)
- **Original**: सा तु तिट्ठति दैत्पेन्द्र तां भवान्‌ द्रष्टमहति
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2785)
- **Original**: यानि रत्नानि मणयो गजाश्मादीनि सै प्रभो
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2786)
- **Original**: ब्रैलोक्ये तु समस्तानि साम्प्रतं धान्ति ते गृहे। 93
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2787)
- **Original**: ऐराबतः समानीतों गजरत्न॑ पुरन्दरात। पारिजाततरुश्लायं॑ तथैबोच्चं: अबा हय:
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2788)
- **Original**: ब्विमान हंससंयुक्तमेतत्तिष्ठति तेउड्डूणें। रत्नभूतमिहानीत॑ बदासीदेथसोउझ्ुतम्‌
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2789)
- **Original**: निश्चिष महापद्य: समानीतों धनेश्वरात्‌। किज्जल्किमी ददी चाब्धिर्पालामप्लानपडुजाम्‌
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2790)
- **Original**: हज ते वारुणं गेहे क्ाझ्जनस्त्रावि तिघुति। तथाय॑ स्पन्दनवरों यः पुरा55सीत्प्रजापते;
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2791)
- **Original**: पृत्वोरुत्क्रान्तिदा नाम शक्तिरीश त्वचा हता। पाशः सलिलराजस्य भ्रातुस्तव परिग्रहे
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2792)
- **Original**: निशुष्भस्थाब्धिजाताश्व समस्ता सक्तजातय:। बहिरपि ददी तुभ्यमग्निशौच्े च वाससी
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2793)
- **Original**: एबं दैत्येन्द्र रल्लानि समस्तान्याइतानिं तें। स्त्रीरल्लमेघा कल्याणी त्वया कस्मान्न गृहाते
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2794)
- **Original**: ऋषि कहते हैं-- 483
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2795)
- **Original**: राजन! इस प्रकार जब देवता स्तुति कर रहे थे, उस समय पार्वती देवी गड्जाजीके जलमें स्तान करनेके लिये वहाँ आर्यी
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2796)
- **Original**: उन सुन्दर भौंहरोंवाली भगवतीने देवताओंसे पूछा--'आपलौग यहाँ किसकी स्तुति करते हैं ?' तब उन्होंके शरीरकोशसे प्रकट हुई शिवादेवी बोलों--
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2797)
- **Original**: “शुम्भदवत्यसे पस्क्ृत और युद्धमें निशुम्भसे पराजित हो यहाँ एकत्रित हुए ये समस्त देवता यह मेरी हो स्वत 43. ण2-क्रोषा। 3. पा0-कपिकों / 4, प0--श्लापि।
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2798)
- **Original**: 208 * संक्षिप्त मार्कपडेयपुराण * #44465:4655%7:54-47:: 45035 कक्ष1575 97754 + #757 # #&+55&5#%6%54&: 55 5 22.2200300:3:2%7 07 0770 7546 44 55525 कर रहे हैं'
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2799)
- **Original**: पार्षत्तीजीके शरीरकोशसे अभ्थिकाका ग्रादुर्भाव हुआ थ्रा, इसलिये ते समस्त लौकोंमे “कॉशिको ' कही जाती हैं
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2800)
- **Original**: कौशिकीके प्रकूट होनेवे: बाद पार्वत्रीदेवोक्ना शरीर काले घरमें शोभा पाता है तथा यह श्रेष्ठ रथ, जो पहले प्रजापतिके अधिकारनें था, अब आपके पास मौजूद है
- **Translation**: 

---

