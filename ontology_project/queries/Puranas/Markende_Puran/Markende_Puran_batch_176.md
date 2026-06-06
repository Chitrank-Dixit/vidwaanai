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

### Verse 1 (Markende Puran 0.3501)
- **Original**: दुर्वत्तानापष्ोधा्णा बलहानिकर॑ परम्‌। रक्षोभूतपिजञाचानां पठनादेज चाशभम्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3502)
- **Original**: संर्त ममैतेन्याहात्म्यं मम सपन्रिधिकारकम्‌। पशुपुष्पाध्यधूपैज्ञ गन्थदीपैस्तथोत्तमै:
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3503)
- **Original**: विप्रार्ण भोजनैहम: प्रोक्षणीयरहरनिशम्‌। अर्च्श्ष विविध्ोंग: प्रदामर्वत्सरेण या
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3504)
- **Original**: प्रीति क्रियते सासम्मित्‌ सकृत्सुचरितें श्रुते। श्रुत॑ं हरतिं पापानि तथा55रोग्से प्रभ्नच्छति
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3505)
- **Original**: रक्षां क्रोति भूतेभ्यो जन्मनां कीर्तन म्रप्त। युद्धेषु चरित यन्मे दुष्दैत्यनिद्ईणम्‌
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3506)
- **Original**: तस्पिज्छुते वैरिकृतं भं पुंसां न जायते। युष्माभि: स्तुतयो याश्ष या क्ष ब्रह्मभिभि; कृता:
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3507)
- **Original**: ब्रह्मणा च कृतास्तास्तु प्रयच्छान्ति शुभां प्रतिम्‌। आरणये प्रान्तों ब्रापि दाबाग्निपरिवारितः
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3508)
- **Original**: 8, झा8-ज्नीक्षिण्यासि। 5,
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3509)
- **Original**: 3--फपर्बाधा। दस्युभिववां थृतः शून्ये गृहीतो वापि शत्रुभि:। सिंहन्पाप्रानुातों श्रा बने बा वनहस्तिभि;
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3510)
- **Original**: गाज्ञा क्ुद्धेन चाज्ञमो सध््यों खन्धगतो5पि वा। आधूर्णितों था चातेन स्थित: पोत्ते महार्णवे
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3511)
- **Original**: सर्वायाथासु घोग़सु वेदनाभ्यर्दितोडपि या
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3512)
- **Original**: स्मसन्‍्ममैंतच्यरिते भरों मुच्येत सड्डटात््‌। मप प्रभावास्सिड्ाद्या दस्यवों बैरिणस्तथा।29
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3513)
- **Original**: दूरादेब पलायन्लें स्मरतश्चरितं ममं
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3514)
- **Original**: देवी बोलीं--
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3515)
- **Original**: देवताओं ! जो एकांग्रनित होकर प्रतिदिन इन स्तुतियोंसे सेरा स्तवन करेगा, उसकी सारों जाधा में निश्चय ही दूर कर
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3516)
- **Original**: जो मधु क्रैटभका नाश, महिषासुस्का बद हथा शुध्भ-निशुम्भके संहारके प्रस॒ज्ञुका पाठ करेंगे
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3517)
- **Original**: तथा अष्टमी, चतुर्दशी और नवमोको भो जो एकाप्रचित्त हो भ्क्तिपूर्वक मेरे उत्तम माहात्म्यका श्रवण करेंगे
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3518)
- **Original**: उन्हें कोई पाप नहों छू सक्रेगा। उनपर पापजनित आपत्तियाँ भो नहीं आयेंगी। उनके श्वरमें कभी दरिद्धता नहीं होगी तथा उनको कभी प्रेमी जनोंके विछोहका कष्ट भी नहीं भोगगा पड़ेगा
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3519)
- **Original**: इतना हो नहों, उन्हें जन्रुसे, लुटेरॉसे, राजासे, शस्त्रसे, ऑनसे तथा जलको राशिसे भी कभी भय उहीं होगा
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3520)
- **Original**: इसलिये सप्तकों एकांग्रचित् होकर भ्क्तिपूर्वक मेरे इस माहात्म्यकों सदा पढ़ना और सुनना चाहिवे। थह परम कल्याणकारक हैं
- **Translation**: 

---

