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

### Verse 1 (Bhagwat Puran 0.281)
- **Original**: फल खानेसे गर्भ रहेगा और गर्भसे पेट बढ़ जाबगा। फिर कुछ खाया-पीया जायेगा नहीं, इससे मेरी शक्ति क्षीण हो जायगी; तब बता, घरका धंधा कैसे होगा ?
- **Translation**: 

---

### Verse 2 (Bhagwat Puran 0.282)
- **Original**: और--दैववश--यदि कहीं. गाँवमें. डाकुओंका
- **Translation**: 

---

### Verse 3 (Bhagwat Puran 0.283)
- **Original**: आतच्ड ] * प्राह्मत््य + 93 है अंश ऑ अं औ घ घी कऐघ घी घी औघ ऑफ के आज लेन ले ओ ओऑ के हे औ के के कै प्रेमी के के को के मे मे ओके मे औो ओ # मे मे ओ मी मी मे ओ कम मे ओ के है औ औ # # है औ औ हे है के क # हे हे आक्रमण हो गया तो गर्भिणी खो कैसे भागेगी। यदि शुकदेवजीकी तरह यह गर्भ भी पेटमें ही रह गया तो इसे बाहर कैसे निकाला जायगा
- **Translation**: 

---

### Verse 4 (Bhagwat Puran 0.284)
- **Original**: ओर कहाँ प्रसवकालके समय वह टेढ़ा हो गया तो फिर फ्राणोंसे ही हाथ घोना पड़ेगा। यों भी प्रसवके समय बड़ी भयंकर पीड़ा होती है; मैं सुकुमारी भला, यह सब कैसे सह सकूँगी ?
- **Translation**: 

---

### Verse 5 (Bhagwat Puran 0.285)
- **Original**: मैं जब दुर्बल पड़ जाऊँगी, तब ननदरानी आकर घरका सब माल-मता समेट ले जायँगी। और मुझसे तो सत्य-शौचादि नियमोंका पालन होना भी कठिन ही जान पड़ता है
- **Translation**: 

---

### Verse 6 (Bhagwat Puran 0.286)
- **Original**: जो खरी बच्चा जनती है, उसे उस बच्चेके लालन-पालनमें भी बड़ा कष्ट होता है। मेरे बिचारंसे तो वख्या या विधवा सख्त्रियाँ ही सुखो हैं'
- **Translation**: 

---

### Verse 7 (Bhagwat Puran 0.287)
- **Original**: मनमें ऐसे ही तरह-तरहके कुततर्क उठनेसे उसने वह फल नहीं खाया और जब उसके पतिने पूछा-- फल खा लिया ?' तब उसने कह दिया--'हाँ, खा लिया'
- **Translation**: 

---

### Verse 8 (Bhagwat Puran 0.288)
- **Original**: एक दिन उसकी बहिन अपने-आप ही उसके घर आयी; तब डसने अपनी बहिनको सा वृत्तान्त सुनाकर कहा कि 'पेरे मनमें इसकी यड़ी चिन्ता है
- **Translation**: 

---

### Verse 9 (Bhagwat Puran 0.289)
- **Original**: मैं इस दुःखके कारण दिनोंदिन दुबली हो रही हूँ। बहिन! मैं क्या वह बालक मैँ तुझे दे दूँगी
- **Translation**: 

---

### Verse 10 (Bhagwat Puran 0.290)
- **Original**: तबतक तू गर्भवतीके समान घरमें गुप्तरूपसे सुखसे रह
- **Translation**: 

---

### Verse 11 (Bhagwat Puran 0.291)
- **Original**: तू मेंरे पतिको कुछ धन दे देगी तो वे तुझे अपना बालक दे देंगे
- **Translation**: 

---

### Verse 12 (Bhagwat Puran 0.292)
- **Original**: (हम ऐसी युक्ति करेंगी) कि जिसमें सब लोग यहीं कहें कि 'इसका बालक छ: महीनेका होकर मर गया' और मैं नित्यप्रति तेरे घर आकर उस ब्रालकका पालन-पोषण करती रहूँगी
- **Translation**: 

---

### Verse 13 (Bhagwat Puran 0.293)
- **Original**: तू इस समय इसकी जाँच करनेके लिये यह फल गौको खिला दे ।' आरह्मणीने स्रीस्वभाववश जो-जों उसकी ऋहिनने कहा था, वैसे ही सब किया
- **Translation**: 

---

### Verse 14 (Bhagwat Puran 0.294)
- **Original**: इसके पश्चात्‌ समयानुसार जब उस स्त्रीके पुत्र हुआ, तब उसके पिताने चुपचाप लाकर उसे धुन्धलीको दे दिया
- **Translation**: 

---

### Verse 15 (Bhagwat Puran 0.295)
- **Original**: और उसने आत्मदेवको सूचना दे दी कि मेरे सुखपूर्वक बालक हो गया है। इस प्रकार आत्मदेवके पुत्र हुआ सुनकर सब लोगोंको बड़ा आनन्द हुआ
- **Translation**: 

---

### Verse 16 (Bhagwat Puran 0.296)
- **Original**: ब्राह्ममने उसका जातकर्म-संस्कार करके ब्राह्मणॉको दान दिया और डसके द्वारपर गाना-बजाना तथा अनेक प्रकारके मालिक कृत्य होने लगे
- **Translation**: 

---

### Verse 17 (Bhagwat Puran 0.297)
- **Original**: धुन्धुलीने अपने पतिसे कहा, “मेरे स्तनोमें तो दूध ही नहीं है; फिर गौ आदि किसी अन्य जीवके दूधसे मैं इस बालकका किस प्रकार पालन करूँगी 2
- **Translation**: 

---

### Verse 18 (Bhagwat Puran 0.298)
- **Original**: मेरी बहिनके अभी बालक हुआ था, वह मर गया है; उसे बुलाकर अपने यहाँ रख लें तो वह आपके इस बच्चेका पालन-पोषण कर लेगी'
- **Translation**: 

---

### Verse 19 (Bhagwat Puran 0.299)
- **Original**: तब पुत्रकी रक्षाके लिये आत्मदेवने वैसा ही। किया तथा माता-धुशधुलोने उस बालकका नाम धुखुकारी रखा
- **Translation**: 

---

### Verse 20 (Bhagwat Puran 0.300)
- **Original**: इसके बाद तोन महीने बोतनेपर उस गौके भी एक मनुष्याकार बच्चा हुआ। वह सबश्लिसुन्दर, दिव्य, निर्मल तथा सुवर्णकी-सी कान्तिवाला था
- **Translation**: 

---

