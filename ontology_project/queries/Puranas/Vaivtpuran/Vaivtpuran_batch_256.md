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

### Verse 1 (Vaivtpuran 13.11262)
- **Original**: यह समाचार सुनकर वे सब-के-सब शोकसे करते उन्हें प्रणाम करके चल दिये। विप्रवर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11263)
- **Original**: व्याकुल हो दौड़ते हुए यमुनातटपर जा पहुँचे नारद! तबसे अबतक सदा ही उस कुण्डका नाम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11264)
- **Original**: और बालकोंके साथ रोने लगे। सारे व्रजवासी सुननेमात्रसे पक्षिराजको कैंपकंपी आ जाती है।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11265)
- **Original**: एकत्र हो रोते-रोते शोकसे मूर्च्छित हो गये। माता यह इतिहास, जो धर्मके मुखसे सुना गया था,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11266)
- **Original**: यशोदा कालियदहमें प्रवेश करने लगीं। यह देख तुमसे कहा गया। अब जिसका प्रकरण चल रहा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11267)
- **Original**: कुछ लोगोंने उन्हें रोका। गोप और गोपियाँ है, श्रीहरिके उस श्रवणसुखद, रहस्ययुक्त तथा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11268)
- **Original**: शोकसे अपने -ही अज्ञोंको पीटने लगीं। कुछ मड्अलमय लीलाचरित्रको सुनो। लोग बिलाप करने लगे और कितने ही व्रजवासी श्रीकृष्ण बहुत देरतक यमुना-जलसे ऊपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11269)
- **Original**: अपनी सुध-बुध खो बैठे। राधा भी यमुनाजीके नहीं उठे । यह जानकर ग्वालबाल दु:खी हो गये।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11270)
- **Original**: उस कुण्डमें घुसने लगीं। यह देख कुछ स्त्रियोंने वे मोहवश यमुनाके तटपर रोने लगे। कुछ बालक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11271)
- **Original**: दौड़कर उन्हें रोका। वे शोकसे मूर्च्छित हो गयीं शोकसे व्याकुल हो अपनी छाती पीटने लगे। कोई श्रीहरिके बिना पृथ्वीपर पछाड़ खाकर गिरे और मूर्च्छित हो गये। कितने ही बालक श्रीकृष्णविरहसे व्यथित हो कालियदहमें प्रवेश करनेको उद्यत हो गये और कुछ ग्वालबाल उनको उसमें जानेसे रोकने लगे। कोई-कोई बिलाप करके प्राण त्याग देनेको उद्यत हो गये और उनमें जो समझदार थे, ऐसे कुछ बालक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11272)
- **Original**: : उन मरणोन्मुख बालकोंकी प्रयलपूर्वक रक्षा करने
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11273)
- **Original**: लगे। कोई 'हाय-हाय' कहकर रोने-बिलखने लगे। कोई “कृष्ण-कृष्ण' की रट लगाने लगे और कोई इस समाचारकों बतानेके लिये नन्दरायजीके समीप दौड़े गये। कुछ बालक वहाँ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11274)
- **Original**: ---- - द शोक, भय और मोहसे आतुर हो परस्पर मिलकर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11275)
- **Original**: और उस नदीके तटपर मरी हुईके समान पड़
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11276)
- **Original**: 502 * संक्षिप्त ब्रह्मवैवर्तपुराण « 2005555% 41444 ###%$% 54% % # 84% 4 %% ऋ#### ### शक ऋऋ ऋऋ# ## # 6 # 4 % # ऋऊ* 5 भर ऋ कक # # 4 # 8 6 # # गयीं। नन्दरायजी अत्यन्त विलाप करके बार-
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11277)
- **Original**: इनकी नाभिसे जो कमल पैदा होता है, उसीसे बार मूच्छित होने लगे। वे चेत होनेपर पुन: रोते
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11278)
- **Original**: ब्रह्माजीका प्राकट्य होता है। जिन्हें एकार्णवके तथा रो-रोकर फिर मूर्च्छित हो जाते थे। उस
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11279)
- **Original**: जलमें भी भय नहीं है, उन्हीं परमेश्वरके लिये समय ज्ञानियोंमें श्रेष्ठ बलरामजीने अत्यन्त विलाप
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11280)
- **Original**: इस कालियदहमें विपत्तिकी सम्भावना कितना करते हुए नन्दको, शोकसे कातर हुई यशोदाको,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11281)
- **Original**: महान्‌ अज्ञान है? पिताजी! यदि एक मच्छर सारे गोपों और गोपाड्ननाओंको, अत्यन्त मूल्छित
- **Translation**: 

---

