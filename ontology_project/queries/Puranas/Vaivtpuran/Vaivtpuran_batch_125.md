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

### Verse 1 (Vaivtpuran 8.2765)
- **Original**: “यदि कोई मनुष्य गड्भाका जल हाथमें लेकर मेरे मन्त्रोंसे पवित्र होकर मुझे देखनेके लिये मेरे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.2766)
- **Original**: प्रतिज्ञा करेगा और फिर उस अपनी की हुई धाममें आयेंगे। ऐसे ही तुम्हें भी यदि स्पष्ट दर्शन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.2767)
- **Original**: प्रतिज्ञाका पालन नहीं करेगा तो बह 'कालसूत्र! करनेकी इच्छा हो तो प्रयत्न करो। शम्भु वहीं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.2768)
- **Original**: नामक नरकका भागी होगा और ब्रह्माको पूरी रहकर मेरी आज्ञाका पालन करें। ब्रह्मन्‌! जगदुरो!
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.2769)
- **Original**: आयुतक उसे वहाँ रहना पड़ेगा।' तुम स्वयं विधाता हो। भगवान्‌ शंकरसे कह दो ब्रह्मन्‌! गोलोकमें देवताओंकी सभा जुड़ी कि 'वे वेदोंके अड्रभूत परम मनोहर विशिष्ट
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.2770)
- **Original**: थी। उसमें भगवान्‌ शंकर जब इस प्रकारकी बात शास्त्र अर्थात्‌ तन्त्रशास्त्रका निर्माण करें। उसमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.2771)
- **Original**: कह चुके, तब अकस्मात्‌ परब्रह्म परिपूर्णतम सम्पूर्ण अभीष्ट फल देनेवाले बहुत-से अपूर्व मन्त्र
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.2772)
- **Original**: भगवान्‌ श्रीकृष्ण भगवती श्रीराधाके साथ वहाँ उद्धृत हों। स्तोत्र, ध्यान, पूजाविधि, मन्त्र और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.2773)
- **Original**: प्रकट हो गये। उन पुरुषोत्तम भगवान्‌ श्रीहरिके कवच--इन सबसे वह ततन्‍्त्रशास्त्र सम्पन्न हो।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.2774)
- **Original**: प्रत्यक्ष दर्शन करनेपर देवताओंकी प्रसन्नताकी मेंरे मन्त्र और कवचका निर्माण करके तुम उसका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.2775)
- **Original**: सीमा नहीं रही। वे उनकी स्तुति करने लगे। यत्रपूर्वक गोपन करो। जो मुझसे विमुख हों, उन्हें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.2776)
- **Original**: . इसके बाद उपस्थित देवताओंने अत्यन्त इसका उपदेश नहीं करना चाहिये। सैकड़ों और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.2777)
- **Original**: आनन्दमें भरकर फिरसे उत्सव मनाया। तत्पश्चात्‌ सहस्रोंमें कोई एक भी तो मेरा सच्चा उपासक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.2778)
- **Original**: समयानुसार भगवान्‌ शंकरने शास्त्रदीपका-- होगा। वे भक्तजन ही मेरे मन्त्रसे पवित्र हों।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.2779)
- **Original**: शास्त्रीय मतको प्रकाशित करनेवाले सात्त्विक यदि शंकर देवसभामें ऐसा शास्त्र निर्माण करनेके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.2780)
- **Original**: तन्त्रशास्त्रका निर्माण किया। लिये सुदृढ़ प्रतिज्ञा करते हैं तो उन्हें तुरन्त हो नारद! इस प्रकार सम्पूर्ण परम गोप्य प्रसड्ढ मेरे दर्शन प्राप्त हो जायँगे।' मैं तुम्हें सुना चुका। यह सबके लिये अत्यन्त आकाशवाणीके द्वारा इस प्रकार कहकर [दुर्लभ है। बे ही पूर्णब्रह्म भगवान्‌ श्रोकृष्ण भगवान्‌ श्रीहरि चुप हो गये। उनकी वाणी सुनकर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.2781)
- **Original**: जलरूप होकर गड्जा बन गये थे। गोलोकसे प्रकट जगत्‌की व्यवस्था करनेवाले ब्रह्माने प्रसन्नतापूर्वक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.2782)
- **Original**: होनेवाली गड्जाका यही रहस्य है। यों भगवान्‌ उसे भगवान्‌ शंकरसे कहा। ज्ञानियोंमें श्रेष्ठ तथा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.2783)
- **Original**: श्रीराधाकृष्ण ही गद्भाके रूपमें प्रकट हुए हैं। ज्ञानके अधिष्ठाता भगवान्‌ शंकरने ब्रह्माकी बात श्रीराधा और श्रीकृष्णके अड्भसे प्रकट हुई सुननेके पश्चात्‌ हाथमें गड्ा-जल ले लिया और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.2784)
- **Original**: यह गड्जा भुक्ति और मुक्ति दोनोंकों देनेवाली आज्ञापालन करनेके लिये प्रतिज्ञा कर ली। फिर
- **Translation**: 

---

