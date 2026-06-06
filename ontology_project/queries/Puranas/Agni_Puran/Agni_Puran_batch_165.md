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

### Verse 1 (Agni Puran 0.3281)
- **Original**: 62--69
- **Translation**: 

---

### Verse 2 (Agni Puran 0.3282)
- **Original**: इस प्रकार आदि आरेय महापुराणमें 'जनत-मरणके अज्लौँचका वर्णत” नामक एक साँ अट्टाकनवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 3 (Agni Puran 0.3283)
- **Original**: >चन्‍0- 22150... एक सौ उनसठवाँ अध्याय असंस्कृत आदिकी शुद्धि पुष्कर कहते हैं-- मृतकका दाह-संस्कार
- **Translation**: 

---

### Verse 4 (Agni Puran 0.3284)
- **Original**: कमलके सदृश नेत्रवाले भगवान्‌ नारायण अविनाशी हुआ हो या नहीं, यदि श्रीहरिका स्मरण किया
- **Translation**: 

---

### Verse 5 (Agni Puran 0.3285)
- **Original**: हैं, अत: उन्हें जो कुछ अर्पण किया जाता है, जाय तो उससे उसको स्वर्ग और मोक्ष --दोनोंकी
- **Translation**: 

---

### Verse 6 (Agni Puran 0.3286)
- **Original**: उसका नाश नहीं होता। भगवान्‌ जनार्दन जीवका प्राप्त हो सकती है।' मृतककी हड्डियोंकों गज्भाजीके
- **Translation**: 

---

### Verse 7 (Agni Puran 0.3287)
- **Original**: पतनसे त्राण (उद्धार) करते हैं, इसलिये वे ही जलमें डालनेसे उस प्रेत (मृत व्यक्ति)-का
- **Translation**: 

---

### Verse 8 (Agni Puran 0.3288)
- **Original**: दानके सर्वोत्तम पात्र हैं
- **Translation**: 

---

### Verse 9 (Agni Puran 0.3289)
- **Original**: अभ्युदय होता है। मनुष्यकी हड्डी जबतक गड़जीके
- **Translation**: 

---

### Verse 10 (Agni Puran 0.3290)
- **Original**: . निश्चय ही नीचे गिरनेवाले जीवॉंको भी भोग जलमें स्थित रहती है, तबतक उसका स्वर्गलोकमें
- **Translation**: 

---

### Verse 11 (Agni Puran 0.3291)
- **Original**: और मोक्ष प्रदान करनेवाले एकमात्र. श्रीहरि ही निवास होता है।' आत्मत्यागी तथा पतित मनुष्योंके
- **Translation**: 

---

### Verse 12 (Agni Puran 0.3292)
- **Original**: हैं। “सम्पूर्ण जगतके लोग एक-न-एक दिन लिये यद्यपि पिण्डोदक-क्रियाका विधान नहीं है
- **Translation**: 

---

### Verse 13 (Agni Puran 0.3293)
- **Original**: मरनेवाले हैं '--यह विचारकर सदा अपने सच्चे तथापि गड्भाजीके जलमें उनकी हड्डियोंका डालना
- **Translation**: 

---

### Verse 14 (Agni Puran 0.3294)
- **Original**: सहायक धर्मका अनुष्ठान करना चाहिये; पतित्रता भी उनके लिये हितकारक ही है। उनके उद्देश्यसे
- **Translation**: 

---

### Verse 15 (Agni Puran 0.3295)
- **Original**: पलीको छोड़कर दूसरा कोई ब्रन्धु-बान्धव मरकर दिया हुआ अन्न और जल आकाशमें लीन हो
- **Translation**: 

---

### Verse 16 (Agni Puran 0.3296)
- **Original**: भी मरे हुए मनुष्यके साथ नहीं जा. सकता; जाता है। पतित प्रेतके प्रति महान्‌ अनुग्रह करके
- **Translation**: 

---

### Verse 17 (Agni Puran 0.3297)
- **Original**: क्योंकि यमलोकका मार्ग सबके लिये अलग- उसके लिये 'नारायण-बलि' करनी चाहिये।। अलग है। जीव कहीं भी क्‍यों न जाय, एकमात्र इससे वह उस अनुग्रहका फल भोगता है।
- **Translation**: 

---

### Verse 18 (Agni Puran 0.3298)
- **Original**: धर्म ही उसके साथ जाता है। जो काम कल 1, “सस्कृतस्थासंस्कृतस्थ स्वर्गों मोश्षो हरिस्पृते: ।" (अग्नि0 159। 1) *मरनेवाला सनुष्य सरनेके समय यदि भगवशामका उच्चारण या भगवत्स्मरज्ञ कर ले, तब तो उसे भगवत्प्राप्ति अवश्य होती है; परंतु अदि उप्सके उद्देश्वसे भगवत्स्मरण किया जाय तो उससे भी उसको स्वर्ग और मोक्ष सुलभ हो सकते हैं।' 2. ' गक़तोयें नरस्थाम्थि याजतावद दिवि स्थिति:
- **Translation**: 

---

### Verse 19 (Agni Puran 0.3299)
- **Original**: * (अग्नि0 159। 2)
- **Translation**: 

---

### Verse 20 (Agni Puran 0.3300)
- **Original**: करना है, उसे आज ही कर ले; जिसे दोपहर
- **Translation**: 

---

