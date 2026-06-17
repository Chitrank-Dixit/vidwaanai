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

### Verse 1 (Markende Puran 0.2401)
- **Original**: सिंहमाहत्व खद्गेन तीक्ष्णयारेण मूर्घनि। आजषधान भुजे सब्ये देवीमप्यतिवेगवान्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2402)
- **Original**: 9 घा0-तेन सब्फाधा न्ती रा तस्या: खड़्गो भुज॑ प्राप्य पफाल नृपनन्दन। ततों जग्राह शूल॑ से कोपादरुणलोचन:
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2403)
- **Original**: चिक्षेप च ततस्तत्तु भद्गकाल्य महासुरः। जाज्वल्यमान॑ त्तेजोभी रधिब्रिप्थमिवाप्खरात्‌
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2404)
- **Original**: दृष्ठा तदापतच्छूलं॑ देवी शूलममुझत। चच्छूल। ज्त्तथा तेव भीत॑ स च्ञ भहासुरः
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2405)
- **Original**: 104 ऋषि कहते हैं--
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2406)
- **Original**: दैत्वोंकी सेनाको इस प्रकार तहंस-संहस होते देख महादँत्य सेनापति चिक्षुर क्रोघपें भरकर अम्बिका देवींसे युद्ध करनेकों आगे बढ़ा
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2407)
- **Original**: वह अंसुर रणभूमिमें देवीके ऊप9 इस प्रकार बा्णोंकी वर्षा करने लगा, जैंसे खादल मेरुगिर्रिके शिखरपर पानीकी धार जरसा रहा हो
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2408)
- **Original**: तब देवोने अपने जाणोंसे उसके बाभ-समूहंकों अनायास हीं काटकर उसके घोड़ों और सारधिको भों गार डाला
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2409)
- **Original**: साथ हो उसके धनुष तथा अत्यन्त ऊँची ध्ठ्लाकों भो तत्काल काट गिराया। धनुष कट जानेपर उसके अज्ञोंको अपने बाणोंसे बाघ डाला
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2410)
- **Original**: धनुष, सथ, घोढ़े और सारधिके नष्ट हो जानेपर वह असुर हाल और तलबार लेकर देखबीक्नी ओर दौड़ा
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2411)
- **Original**: उसने ततोखी धारवाली तलबारसे सिंहके मस्तकपर चोट करके देवीकी भी बायों भुजामें बड़े वेगसे प्रहार किया
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2412)
- **Original**: राजन! देवीकी जाहपर पहुँचते ही त्रह तलवार ट्रूटट गयो, फिर तो क्रोधसे लाल आँखें करके उस शराक्षसने श्ूल हाथमें ल्िया
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2413)
- **Original**: और उसे ढस महादैत्ववे भगवतो भद्रकालीके ऊपर चलाबा। नह शूल आकाशसे गिस्ते हुए सुर्यमण्डलकी मोति अपने तेजसे प्रण्वालत हो उठा
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2414)
- **Original**: 5स शूलकों अपनी
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2415)
- **Original**: 199 *मंश्षित्त सार्कण्डेयपुराण « 33707 %317 # # #
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2416)
- **Original**: 77 44 4 # 88 :4:5 55:53 7:2::2 77% 21729 47477:7 7447 ## 8 & 68 854 2522:2702:293.%9/*/7+ 44 655:4473 535 आर शाते देख द्ेत्लीनी भो शूल्क। प्रहार किया। उससे गशक्षसके शुलके सैकड़ों टुकड़े हो गये साथ हो मड़ादैत्य चिक्षुक्तों भी धज्जियाँ डड गयाँ। घह प्रणोंसे हाथ भो बैटा
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2417)
- **Original**: इते तस्मिमदाबीर्ये महिषस्थ चमूपतो। आजगाप गज़ारूदश्चामरस्म्रिदशारदन:
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2418)
- **Original**: 11 # सो5ए शक्ति पुमोचाथ देव्वास्तापम्बिका द्रुतम्‌। रुंक्काराभिहतां भुमौ पातयामास निष्प्रभाप्‌
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2419)
- **Original**: भ्रग्वां शक्ति निपतितां दृष्ठा क्रोधसमन्वित:। चिक्षेप चापर: शूलं वार्फँस्‍्तदपि साच्छिनतू
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2420)
- **Original**: ततः सिंह: समुत्यत्य गजकुशभान्तरे स्थित: । तत्तो वेगात्ख़मुत्पत्य निपत्य अझ मृगारिणा। क्रप्रहरेण. शिरक्षामरस्थ पृश्रक्नतम्‌
- **Translation**: 

---

