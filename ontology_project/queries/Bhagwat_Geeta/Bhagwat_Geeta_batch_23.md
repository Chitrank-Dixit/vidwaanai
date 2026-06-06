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

### Verse 1 (Bhagwat_Geeta 6.591)
- **Original**: * अध्याय 6*% 879 शुचौ देशे प्रतिष्ठाप्प स्थिरमासनमात्मन: । नात्युच्छितं नातिनीच चैलाजिनकुशोत्तरम्‌
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 6.592)
- **Original**: शुद्ध भूमिमें, जिसके ऊपर क्रमश: कुशा, मृगछाला और वस्त्र बिछे हैं, जो न बहुत ऊँचा है और न बहुत नीचा, ऐसे अपने आसनको स्थिर स्थापन करके--
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 6.593)
- **Original**: तत्रैकाग्रं मनः कृत्वा यतचित्तेन्द्रियक्रिय:ः । उपविश्यासने युज्ज्याद्योगमात्मविशुद्धये
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 6.594)
- **Original**: उस आसनपर बैठकर चित्त और इन्द्रियोंकी क्रियाओंको वशमें रखते हुए मनको एकाग्र करके अन्तःकरणकी शुद्धिके लिये योगका अभ्यास करे
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 6.595)
- **Original**: समं॑ कायशिरोग्रीवं॑ धारयन्नचलं स्थिरः। सम्प्रेक्ष्य नासिकाग्र॑ स्व॑ दिशश्चानवलोकयन्‌
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 6.596)
- **Original**: काया, सिर और गलेको समान एवं अचल धारण करके और स्थिर होकर, अपनी नासिकाके अग्रभागपर दृष्टि जमाकर, अन्य दिशाओंको न देखता हुआ--
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 6.597)
- **Original**: प्रशान्तात्मा विगतभीर्रहाचारिब्रते स्थितः । मन: संयम्य मच्चित्तो युक्त आसीत मत्पर:
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 6.598)
- **Original**: ब्रह्मचारीके ब्रतमें स्थित, भयरहित तथा भलीभाँति
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 6.599)
- **Original**: 88 * श्रीमद्धगवद्रीता * शान्त अन्तःकरणवाला सावधान योगी मनको रोककर मुझमें चित्तवाला और मेरे परायण होकर स्थित होवे
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 6.600)
- **Original**: युझ्जन्नेव॑ सदात्मानं योगी नियतमानस:। शान्ति निर्वाणपरमां मत्संस्थामधिगच्छति
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 6.601)
- **Original**: वशमें किये हुए मनवाला योगी इस प्रकार आत्माको निरन्तर मुझ परमेश्वरके स्वरूपमें लगाता हुआ मुझमें रहनेवाली परमानन्दकी पराकाष्ठारूप शान्तिको प्राप्त होता है
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 6.602)
- **Original**: नात्यश्वतस्तु योगो5स्ति न चैकान्तमनश्नतः । न चाति स्वप्रशीलस्य जाग्रतो नैव चार्जुन
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 6.603)
- **Original**: हे अर्जुन! यह योग न तो बहुत खानेवालेका, न बिलकुल न खानेवालेका, न बहुत शयन करनेके स्वभाववालेका और न सदा जागनेवालेका ही सिद्ध होता है
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 6.604)
- **Original**: युक्ताहारविहारस्य॒युक्तचेष्टस्य कर्मसु। युक्तस्वप्रावबो धस्य योगो भवति दुःखहा
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 6.605)
- **Original**: दुःखोंका नाश करनेवाला योग तो यथायोग्य आहार-विहार करनेवालेका, कर्मोमें यथायोग्य चेष्टा करनेवालेका और यथायोग्य सोने तथा जागनेवालेका ही सिद्ध होता है
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 6.606)
- **Original**: * अध्याय 6*% 89 यदा विनियतं चित्तमात्मन्येवावतिष्ठते। निःस्पृहः सर्वकामेभ्यो युक्त इत्युच्यते तदा
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 6.607)
- **Original**: अत्यन्त वशमें किया हुआ चित्त जिस कालमें परमात्मामें ही भलीभाँति स्थित हो जाता है, उस कालमें सम्पूर्ण भोगोंसे स्पृहारहित पुरुष योगयुक्त है, ऐसा कहा जाता है
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 6.608)
- **Original**: यथा दीपो निवातस्थो नेड़ते सोपमा स्मृता। योगिनो यतचित्तस्य युद्धतो योगमात्मनः
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 6.609)
- **Original**: जिस प्रकार वायुरहित स्थानमें स्थित दीपक चलाय- मान नहीं होता, वैसी ही उपमा परमात्माके ध्यानमें लगे हुए योगीके जीते हुए चित्तकी कही गयी है
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 6.610)
- **Original**: यत्रोपरमते चित्त निरुद्ध॑ं योगसेवया। यत्र चैवात्मनात्मानं पश्यन्नात्मनि तुष्यति
- **Translation**: 

---

