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

### Verse 1 (Vaivtpuran 13.10802)
- **Original**: तथा मुख शरत्कालके पूर्णचन्द्रकी भाँति परम उनका नाम वृषभानु हुआ। वे सुरभानुके वीर्य मनोहर था। एक दिन गजराजकौ-सी मन्दगतिसे और पद्मावतीके गर्भसे उत्पन्न हुए। उन्हें पूर्वजन्मकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10803)
- **Original**: चलनेवाली राजकुमारी राजमार्गसे कहीं जा रही बातोंका स्मरण था। वे श्रोहरिके अंश थे और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10804)
- **Original**: थी। नन्दजीने उसे मार्गमें देखा। देखकर वे जैसे शुक्लपक्षमें चन्द्रमा बढ़ते हैं, उसी प्रकार
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10805)
- **Original**: बड़े प्रसन्न हुए। उन्होंने उस मार्गसे आने- ब्रजधाममें प्रतिदिन बढ़ने लगे। धीरे-धीरे वे जानेवाले लोगोंसे आदरपूर्वक पूछा--'यह व्रजके अधिपति हुए। उन्हें सर्वज्ञ और महायोगी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10806)
- **Original**: किसकी कन्या जा रही थी।' लोगोंने बताया-- यह माना गया है। उनका चित्त सदा श्रीहरिके महाराज भनन्दनकी कन्या है। इसका नाम चरणारविन्दोंके चिन्तनमें ही लगा रहता था। वे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10807)
- **Original**: कलावती है। यह धन्या बाला लक्ष्मीजीके अंशसे उदार, रूपवान्‌, गुणवान्‌ और श्रेष्ठ बुद्धिवाले थे। राजमन्दिरमें प्रकट हुई है और कौतुकबश कलावती कान्यकुब्ज देशमें उत्पन्न हुई। वह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10808)
- **Original**: खेलनेके लिये अपनी सहेलीके घर जा रही है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10809)
- **Original**: ड82 + संक्षिप्त ब्रह्मवैवर्तपुराण * ऋककककऊकऋऋ कक # 4 #&# ## #######ऋ## कक अंक अंक 5#%% 55:68 88 व्रजराज! आप ब्रजको पधारिये।' ऐसा उत्तर देकर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10810)
- **Original**: गया है। अन्यथा असमर्थ पुरुषके उद्यमको भाँति लोग चले गये। नन्दके मनमें बड़ा हर्ष हुआ।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10811)
- **Original**: सारा कर्म निष्फल हो जाता है। यदि विधाताने वे राजभवनको गये। रथसे उतरकर उन्होंने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10812)
- **Original**: मेरी पुत्रीकों ही वृषभानुकी पत्नी होनेकी बात तत्काल ही राजसभामें प्रवेश किया। राजा उठकर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10813)
- **Original**: लिखो है तो वह पहलेसे ही उनकी पतली है। खड़े हो गये। उन्होंने नन्दरायजीसे बातचीत की
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10814)
- **Original**: मैं फिर कौन हूँ, जो उसमें बाधा डाल सकूँ और उन्हें बैठनेके लिये सोनेका सिंहासन दिया।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10815)
- **Original**: तथा दूसरा भी कौन उस सम्बन्धका निवारण उन दोनोंमें परस्पर बहुत प्रेमालाप हुआ।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10816)
- **Original**: कर सकता है? फिर नन्दने विनीत होकर राजासे सम्बन्धी, नारद! यों कहकर राजेन्द्र भनन्दनने विनयसे बात चलावी।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10817)
- **Original**: सिर झुकाकर नन्दरायजीको आदरपूर्वक मिष्टान्न नन्दजीने कहा--राजेन्द्र! सुनिये। मैं एक
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10818)
- **Original**: भोजन कराया। तत्पश्चात्‌ राजाकी अनुमति ले शुभ एवं विशेष बात कह रहा हूँ। आप इस
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10819)
- **Original**: ब्रजराज ब्रजको लौट गये। जाकर उन्होंने समय अपनी कन्याका सम्बन्ध एक विशिष्ट
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10820)
- **Original**: सुरभानुकी सभामें सब बातें बतायीं। सुरभानुने पुरुषके साथ स्थापित कीजिये। ब्रजमें सुरभानुके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10821)
- **Original**: भी यलपूर्वक नन्‍द और गर्गजीके सहयोगसे सादर पुत्र श्रीमान्‌ वृषभानु निवास करते हैं, जो व्रजके
- **Translation**: 

---

